import os
import cv2
from ultralytics import YOLO
from PIL import Image, ImageTk
import tkinter as tk

# Model ve sınıf tanımları
model = YOLO('yolov8m.pt')
target_classes = ['car', 'bus', 'motorcycle', 'truck', 'bicycle']
class_names = model.names

colors = {
    'car': (0, 255, 0),
    'bus': (0, 0, 255),
    'motorcycle': (255, 0, 0),
    'truck': (0, 165, 255),
    'bicycle': (255, 255, 0)
}

folder_path = 'arac_fotograflari'
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

processed_images = []

# Görselleri işleme
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

    # BGR'dan RGB'ye çevir ve PIL formatına dönüştür
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    processed_images.append(pil_img)

# Tkinter arayüzü
class ImageViewer:
    def __init__(self, root, images):
        self.root = root
        self.images = images
        self.index = 0

        self.label = tk.Label(root)
        self.label.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.prev_button = tk.Button(self.btn_frame, text='<< Geri', command=self.show_prev)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.btn_frame, text='İleri >>', command=self.show_next)
        self.next_button.grid(row=0, column=1, padx=5)

        self.show_image()

    def show_image(self):
        img = self.images[self.index]
        tk_img = ImageTk.PhotoImage(img)
        self.label.config(image=tk_img)
        self.label.image = tk_img  # Referansı sakla

    def show_prev(self):
        self.index = (self.index - 1) % len(self.images)
        self.show_image()

    def show_next(self):
        self.index = (self.index + 1) % len(self.images)
        self.show_image()

# Ana Tkinter penceresini başlat
root = tk.Tk()
root.title("Araç Türü Tespiti")
viewer = ImageViewer(root, processed_images)
root.mainloop()
