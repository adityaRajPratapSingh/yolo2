#yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define path to the image file
source = 'https://ultralytics.com/images/bus.jpg'

# Run inference on the source
results = model(source)  # list of Results objects
