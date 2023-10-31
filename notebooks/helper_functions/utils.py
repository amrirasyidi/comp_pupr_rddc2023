import shutil
from pathlib import Path

from pascal import annotation_from_xml


def convert_and_reorg(xml, img, destination_folder, class_mapping, copy):
    # read xml file
    ann = annotation_from_xml(xml)

    # get ann str
    yolo_ann = ann.to_yolo(class_mapping)

    # save yolo format file
    with open((destination_folder / "labels" / Path(xml).name).with_suffix(".txt"), "w") as f:
        f.write(yolo_ann)
        f.close()
    if copy:
        shutil.copy(img, destination_folder / "images" / Path(img).name)
    else:
        shutil.move(img, destination_folder / "images" / Path(img).name)

def remove_ann_classes(txt, class_to_exclude):
    # Read the annotation file, filter lines based on class labels, and write back to the file
    with open(txt, 'r') as file:
        lines = file.readlines()

    with open(txt, 'w') as file:
        for line in lines:
            # Split the line into components
            parts = line.split()
            if len(parts) > 0:
                class_label = parts[0]
                if class_label not in class_to_exclude:
                    file.write(line)

def class_remap(txt, class_map):
    with open(txt, 'r') as file:
        lines = file.readlines()

    with open(txt, 'w') as file:
        for line in lines:
            # Split the line into components
            parts = line.split()
            # remap the first class id
            parts[0] = class_map[parts[0]]
            file.write(' '.join(parts)+'\n')
