from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import torch
import torch.nn as nn
import joblib
import numpy as np
import os

# Define the model architecture (must be identical to training)
class PlanetPredict(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(in_features=5, out_features=128)
        self.layer2 = nn.Linear(in_features=128, out_features=64)
        self.layer3 = nn.Linear(in_features=64, out_features=32)
        self.layer4 = nn.Linear(in_features=32, out_features=16)
        self.layer5 = nn.Linear(in_features=16, out_features=1)
        self.relu = nn.ReLU()

    def forward(self, X: torch.tensor):
        return self.layer5(self.relu(self.layer4(self.relu(self.layer3(self.relu(self.layer2(self.relu(self.layer1(X)))))))))

app = FastAPI()

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "saved_model", "best_model.pth")
SCALER_X_PATH = os.path.join(BASE_DIR, "saved_model", "scaler_X.joblib")
SCALER_Y_PATH = os.path.join(BASE_DIR, "saved_model", "scaler_y.joblib")

# Load model and scalers
device = torch.device("cpu")
model = PlanetPredict()

if os.path.exists(MODEL_PATH):
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device, weights_only=True))
    model.eval()
else:
    print(f"Error: Model not found at {MODEL_PATH}")

if os.path.exists(SCALER_X_PATH) and os.path.exists(SCALER_Y_PATH):
    scaler_X = joblib.load(SCALER_X_PATH)
    scaler_y = joblib.load(SCALER_Y_PATH)
else:
    print("Error: Scalers not found.")

class PredictionInput(BaseModel):
    pl_orbsmax: float
    st_mass: float
    pl_orbeccen: float
    st_rad: float
    pl_rade: float

@app.post("/predict")
async def predict(data: PredictionInput):
    try:
        # Prepare input
        input_data = np.array([[
            data.pl_orbsmax,
            data.st_mass,
            data.pl_orbeccen,
            data.st_rad,
            data.pl_rade
        ]])
        
        # Scale input
        input_scaled = scaler_X.transform(input_data)
        input_tensor = torch.tensor(input_scaled, dtype=torch.float32)
        
        # Inference
        with torch.no_grad():
            prediction_scaled = model(input_tensor).numpy()
        
        # Inverse scale result
        prediction_log = scaler_y.inverse_transform(prediction_scaled)
        
        # Expm1 (inverse of log1p)
        prediction_final = np.expm1(prediction_log)[0][0]
        
        return {"prediction": float(prediction_final)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve static files from the 'static' directory within 'web_app'
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
