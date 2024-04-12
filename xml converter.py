import os
import xml.etree.ElementTree as ET

# Function to convert bounding box coordinates to YOLO format
def convert_to_yolo_format(x_min, y_min, x_max, y_max, image_width, image_height):
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min
    x_center_norm = x_center / image_width
    y_center_norm = y_center / image_height
    width_norm = width / image_width
    height_norm = height / image_height
    return f"0 {x_center_norm} {y_center_norm} {width_norm} {height_norm}\n"

# Path to XML annotations directory
xml_dir = 'D:\\cool datasets\\masks\\labels'

# Path to save YOLO annotations
yolo_dir = 'D:\\cool datasets\\masks\\labels2'

# Create YOLO annotations directory if it doesn't exist
os.makedirs(yolo_dir, exist_ok=True)

# Iterate over XML files
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith('.xml'):
        # Parse XML file
        tree = ET.parse(os.path.join(xml_dir, xml_file))
        root = tree.getroot()

        # Get image dimensions
        image_width = int(root.find('size/width').text)
        image_height = int(root.find('size/height').text)

        # Open YOLO annotation file
        yolo_filename = os.path.splitext(xml_file)[0] + '.txt'
        with open(os.path.join(yolo_dir, yolo_filename), 'w') as yolo_file:
            # Iterate over object annotations
            for obj in root.findall('object'):
                #class_name = obj.find('name').text
                # Convert bounding box coordinates to YOLO format
                bbox = obj.find('bndbox')
                x_min = int(bbox.find('xmin').text)
                y_min = int(bbox.find('ymin').text)
                x_max = int(bbox.find('xmax').text)
                y_max = int(bbox.find('ymax').text)
                yolo_line = convert_to_yolo_format(x_min, y_min, x_max, y_max, image_width, image_height)
                #yolo_file.write(f"{class_name} {yolo_line}")
                yolo_file.write(f"{yolo_line}")
