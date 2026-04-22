import pandas as pd
import numpy as np
import torch
import joblib
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
import os

# Load dataset
df = pd.read_csv("dataset/space.csv")
df_model = df[["pl_orbper", "pl_orbsmax", "st_mass", "pl_orbeccen", "st_rad", "pl_rade"]]

# Preprocessing (same as in notebook)
df_model = df_model.dropna(subset=["pl_orbper"])
df_model = df_model.fillna(df_model.median())

X = df_model[["pl_orbsmax", "st_mass", "pl_orbeccen", "st_rad", "pl_rade"]].values
y = df_model["pl_orbper"].values
y = np.log1p(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit scalers
scaler_X = RobustScaler()
scaler_y = RobustScaler()

scaler_X.fit(X_train)
scaler_y.fit(y_train.reshape(-1, 1))

# Create directory if not exists
if not os.path.exists("saved_model"):
    os.makedirs("saved_model")

# Save scalers
joblib.dump(scaler_X, "saved_model/scaler_X.joblib")
joblib.dump(scaler_y, "saved_model/scaler_y.joblib")

print("Scalers saved successfully in saved_model/ directory.")
