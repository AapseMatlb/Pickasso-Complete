import cv2
import torch

# Load Pre-trained YOLO Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

def run_inference(image_path):
    img = cv2.imread(image_path)
    results = model(img)
    results.print()  # Logs detected objects
    results.show()  # Visualize results

if __name__ == "__main__":
    run_inference("sample_image.jpg")
