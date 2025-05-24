# 🚗 Araç Türü Tespit Sistemi

Bu proje, Ultralytics YOLOv8 modelini kullanarak kamera veya görsellerdeki taşıt türlerini (araba, otobüs, motosiklet, kamyon, bisiklet) tespit eden bir gerçek zamanlı yapay zekâ uygulamasıdır. Görseller arası geçiş Tkinter ile sağlanmaktadır.

---

## 🎯 Projenin Amacı

Projenin amacı, görsellerdeki araç türlerini sınıflandırarak farklı taşıtları (car, bus, truck, motorcycle, bicycle) otomatik olarak tanımaktır. Özellikle trafik analizi, akıllı şehir uygulamaları ve otonom sürüş sistemleri gibi alanlarda kullanılabilir.

---

## 👥 Hedef Kullanıcı Kitlesi

- Yapay zekâ ve bilgisayarla görme konularına ilgi duyan öğrenciler  
- Trafik verisi analiziyle ilgilenen yazılım geliştiriciler  
- Görüntü işleme ve nesne tanıma alanında çalışan akademisyenler

---

## 🧰 Kullanılan Teknolojiler

- Python 3.10  
- OpenCV 4.x  
- Ultralytics YOLOv8  
- Tkinter (grafik arayüz)  
- PIL (Pillow)  
- NumPy

---

## 🛠️ Kurulum Adımları

```bash
# Gerekli kütüphaneleri yükleyin
pip install ultralytics opencv-python pillow numpy
```
Program çalıştığında klasördeki tüm araç fotoğrafları işlenir ve etiketlenmiş görüntüler, Tkinter arayüzü ile sırayla gösterilir. Kullanıcı ileri ve geri düğmeleri ile geçiş yapabilir.
