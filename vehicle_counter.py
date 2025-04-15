# vehicle_counter.py

from ultralytics import YOLO
import cv2

def count_vehicles(image_path):
    # Load the YOLO model
    model = YOLO("yolov8n.pt")  # You can use yolov8s.pt or yolov8m.pt for better accuracy

    # Read the image
    image = cv2.imread(image_path)

    # Run detection
    results = model(image)

    # Define vehicle classes
    vehicle_classes = ['car', 'truck', 'bus', 'motorcycle']
    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            if class_name in vehicle_classes:
                vehicle_count += 1

    return vehicle_count, results[0]

# Run directly
if __name__ == "__main__":
    image_path = "your_image.jpg"  # Replace this with your input image
    count, result = count_vehicles(image_path)
    print(f"Vehicles Detected: {count}")
    result.show()  # Show bounding boxes
