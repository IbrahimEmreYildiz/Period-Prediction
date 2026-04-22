# Exoplanet Orbital Period Prediction (Ötegezegen Yörünge Periyodu Tahmini)

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🌌 English Description

This project features a deep learning model that predicts the orbital periods of exoplanets using data from NASA's Kepler mission, along with a modern web application to serve the model.

### 🚀 Features
- **Deep Learning Model**: High-accuracy regression model built with PyTorch.
- **Modern Web Interface**: FastAPI-based backend with a responsive "Deep Space" themed frontend.
- **Data Preprocessing**: Automatic scaling and logarithmic transformations for robust predictions.
- **Comparative Analysis**: Instant comparison between predicted values and actual results.

### 📁 Project Structure
```text
period_prediction/
├── dataset/                  # Raw and processed datasets
├── saved_model/              # Trained model (.pth) and scalers (.joblib)
├── web_app/                  # FastAPI application
│   ├── main.py               # Backend API
│   └── static/               # Frontend files (HTML, CSS, JS)
├── data_pre-processing.ipynb # Data analysis and preprocessing notebook
├── save_scalers.py           # Script to prepare scalers for model inputs
├── .gitignore                # Files to be ignored by Git
└── README.md                 # Project documentation
```

### 🛠️ Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd period_prediction
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # For Windows:
   .\venv\Scripts\activate
   # For Linux/macOS:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn torch joblib scikit-learn pandas numpy
   ```

### 💻 Usage
To start the web application:
```bash
cd web_app
python main.py
```
The app will run at `http://127.0.0.1:8000`. Enter exoplanet parameters to get orbital period predictions.

---

<a name="türkçe"></a>
## 🌌 Türkçe Açıklama

Bu proje, NASA'nın Kepler görevinden elde edilen verileri kullanarak ötegezegenlerin yörünge periyotlarını tahmin eden bir derin öğrenme modelini ve bu modeli sunan modern bir web uygulamasını içerir.

### 🚀 Özellikler
- **Derin Öğrenme Modeli**: PyTorch kullanılarak eğitilmiş, yüksek doğruluklu regresyon modeli.
- **Modern Web Arayüzü**: FastAPI tabanlı backend ve "Deep Space" temalı, responsive frontend.
- **Veri Ön İşleme**: Otomatik ölçeklendirme (Scaling) ve logaritmik dönüşümler.
- **Karşılaştırmalı Analiz**: Tahmin edilen değerlerin gerçek değerlerle anlık karşılaştırması.

### 📁 Proje Yapısı
(Yukarıdaki İngilizce bölümde detaylandırılmıştır.)

### 🛠️ Kurulum
1. **Depoyu klonlayın:**
   ```bash
   git clone <repo-url>
   cd period_prediction
   ```
2. **Sanal ortam oluşturun ve aktif edin:**
   ```bash
   python -m venv venv
   # Windows için:
   .\venv\Scripts\activate
   # Linux/macOS için:
   source venv/bin/activate
   ```
3. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install fastapi uvicorn torch joblib scikit-learn pandas numpy
   ```

### 💻 Kullanım
Web uygulamasını başlatmak için:
```bash
cd web_app
python main.py
```
Uygulama `http://127.0.0.1:8000` adresinde çalışacaktır. Ötegezegen parametrelerini girerek tahminler alabilirsiniz.

---
## 👤 Author / Geliştirici

**İbrahim Emre Yıldız**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ibrahim-emre-yıldız-549ab0256)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IbrahimEmreYildiz)



