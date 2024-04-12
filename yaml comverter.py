import os
import yaml


def convert(x_center, y_center, width, height, image_width, image_height):
    x_center_norm = x_center / image_width
    y_center_norm = y_center / image_height
    width_norm = width / image_width
    height_norm = height / image_height
    return f"0 {x_center_norm} {y_center_norm} {width_norm} {height_norm}\n"
    # the f states that this is a formatted string literal
    # in the quotes the 0 means that there is only a single class of objects denoted using 0
    #{} are the placeholders for the variables inside


annotations_dir = "D:\\cool datasets\\masks\\labels"
output_dir = "D:\\cool datasets\\masks\\labels_2"

os.makedirs(output_dir,exist_ok=True)  #to make a new directory the 1st arg is the path and the second specifies if there is an error if the directoy already exists or not

for yaml_file in os.listdir(annotations_dir):
    if yaml_file.endswith('.yaml'):
        with open(os.path.join(annotations_dir,yaml_file),'r') as file:
            annotations=yaml.safe_load(file)
        output_file = os.path.splitext(yaml_file)[0] + '.txt'  #if the name of the yaml file is example.yaml then the splitext will split the name into a tuple like example and .yaml and then take the index 0 element and concatenate it with the .txt extension
        with open((os.path.join(output_dir,output_file)),'w') as yolo_file:

            for annotation in annotations:
                image_path = annotation['image_path']
                image_width = annotation['image_width']
                image_height = annotation['image_height']
                for bbox in annotation['annotations']:
                    x_center = bbox['x'] + bbox['width'] / 2
                    y_center = bbox['y'] + bbox['height'] / 2
                    yolo_line = convert(x_center, y_center, bbox['width'], bbox['height'], image_width, image_height)
                    yolo_file.write(f"{image_path} {yolo_line}")