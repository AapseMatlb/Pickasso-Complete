import cv2
import torch
from category_mapping import map_category
import requests

# Convex API URL (replace with your actual URL)
CONVEX_API_URL = "https://<your-convex-app-url>/api/updateStatus"

# Load YOLOv5 Pre-trained Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

def update_hmi(task, reason):
    payload = {"task": task, "reason": reason, "battery": "100%"}
    try:
        requests.post(CONVEX_API_URL, json=payload)
    except Exception as e:
        print(f"[HMI Update Error]: {e}")

def run_inference(image_path):
    img = cv2.imread(image_path)
    results = model(img)
    detected_objects = results.pandas().xyxy[0]['name'].tolist()

    for obj in detected_objects:
        category = map_category(obj)
        print(f"[Vision] Detected: {obj} | Mapped Category: {category}")
        update_hmi("Object Detected", f"Detected {category} item: {obj}")

    results.show()

if __name__ == "__main__":
    run_inference("sample_image.jpg")
