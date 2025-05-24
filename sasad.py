from ultralytics import YOLO
import cv2
import os

model = YOLO('yolov8m.pt')

target_classes = ['car', 'bus', 'motorcycle', 'truck', 'bicycle']
class_names = model.names

# Araç türlerine özel renkler (BGR)
colors = {
    'car': (0, 255, 0),        # Yeşil
    'bus': (0, 0, 255),        # Kırmızı
    'motorcycle': (255, 0, 0), # Mavi
    'truck': (0, 165, 255),    # Turuncu
    'bicycle': (255, 255, 0)   # Sarı
}

folder_path = 'arac_fotograflari'
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    results = model(image_path)
    img = cv2.imread(image_path)

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls.cpu().numpy())
            conf = float(box.conf.cpu().numpy())
            label = class_names[cls_id]

            if label in target_classes and conf > 0.3:
                x1, y1, x2, y2 = map(int, box.xyxy.cpu().numpy()[0])
                width = x2 - x1
                height = y2 - y1
                area = width * height

                # Truck için küçük alanlı kutuları filtrele
                if label == 'truck' and area < 5000:
                    continue

                color = colors.get(label, (0, 255, 0))

                font_scale = 0.6
                font = cv2.FONT_HERSHEY_SIMPLEX
                thickness = 2

                text_size, _ = cv2.getTextSize(label, font, font_scale, thickness)
                text_w, text_h = text_size

                text_bg_x1 = x1
                text_bg_y1 = max(0, y1 - text_h - 5)
                text_bg_x2 = x1 + text_w
                text_bg_y2 = y1

                cv2.rectangle(img, (text_bg_x1, text_bg_y1), (text_bg_x2, text_bg_y2), color, cv2.FILLED)
                cv2.putText(img, label, (x1, y1 - 5), font, font_scale, (0, 0, 0), thickness)

                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

    cv2.imshow('Araç Türü Tespiti', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
