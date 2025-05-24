# 🚗 Araç Türü Tespiti (YOLOv8 + OpenCV)

Bu proje, **YOLOv8 (You Only Look Once)** nesne algılama modeli kullanılarak görüntülerdeki araç türlerini (araba, otobüs, motosiklet, kamyon, bisiklet) tespit eder ve her birini sınıfa özel renklerle kutular içine alarak görselleştirir.

# Özellikler

- YOLOv8 modelini kullanarak yüksek doğrulukla araç algılama.
- Sadece belirli araç sınıfları üzerinde işlem yapılır: `car`, `bus`, `motorcycle`, `truck`, `bicycle`.
- Her araç türü için özel renkler tanımlanır.
- Küçük boyutlu kamyon kutuları (örneğin uzaktaki tespitler) otomatik olarak filtrelenir.
- Her görsel işlendikten sonra tespit sonuçları OpenCV ile gösterilir.

---

## 📦 Gereksinimler

Aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:

```bash
pip install ultralytics opencv-python

proje_dizini/
├── arac_fotograflari/         # Girdi görsellerini buraya yerleştirin
├── yolov8_arac_tespiti.py     # Ana Python betiği
└── README.md                  # Bu dökümantasyon dosyası
