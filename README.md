# Exoplanet Orbital Period Prediction (Ötegezegen Yörünge Periyodu Tahmini)

Bu proje, NASA'nın Kepler görevinden elde edilen verileri kullanarak ötegezegenlerin yörünge periyotlarını tahmin eden bir derin öğrenme modelini ve bu modeli sunan bir web uygulamasını içerir.

## 🚀 Özellikler

- **Derin Öğrenme Modeli**: PyTorch kullanılarak eğitilmiş, yüksek doğruluklu regresyon modeli.
- **Modern Web Arayüzü**: FastAPI tabanlı backend ve "Deep Space" temalı, responsive frontend.
- **Veri Ön İşleme**: Otomatik ölçeklendirme (Scaling) ve logaritmik dönüşümler.
- **Karşılaştırmalı Analiz**: Tahmin edilen değerlerin gerçek değerlerle anlık karşılaştırması.

## 📁 Proje Yapısı

```text
period_prediction/
├── dataset/                  # Ham ve işlenmiş veri setleri
├── saved_model/              # Eğitilmiş model (.pth) ve ölçeklendiriciler (.joblib)
├── web_app/                  # FastAPI uygulaması
│   ├── main.py               # Backend API
│   └── static/               # Frontend dosyaları (HTML, CSS, JS)
├── data_pre-processing.ipynb # Veri analizi ve ön işleme not defteri
├── save_scalers.py           # Model girişleri için ölçeklendirici hazırlama betiği
├── .gitignore                # Git tarafından yoksayılacak dosyalar
└── README.md                 # Proje dokümantasyonu
```

## 🛠️ Kurulum

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

## 💻 Kullanım

Web uygulamasını başlatmak için:

```bash
cd web_app
python main.py
```

Uygulama varsayılan olarak `http://127.0.0.1:8000` adresinde çalışacaktır. Tarayıcınızdan bu adrese giderek ötegezegen parametrelerini girebilir ve yörünge periyodu tahminlerini alabilirsiniz.

## 🧪 Model Detayları

Model, giriş parametreleri olarak gezegen yarıçapı, yıldız kütlesi, denge sıcaklığı gibi özellikleri alır. Veriler `StandardScaler` ile normalize edilmiş ve hedef değişken logaritmik ölçekte eğitilmiştir.

---
*Bu proje Advanced Agentic Coding çalışmaları kapsamında Antigravity tarafından geliştirilmiştir.*
