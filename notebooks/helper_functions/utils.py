import shutil
from pathlib import Path
from typing import Dict, List

from pascal import annotation_from_xml


def convert_and_reorg(
    xml:str,
    img:str,
    destination_folder:Path,
    class_mapping:Dict,
    copy:bool
):
    """Convert the annotation from pascal VOC (xml) to yolo (txt) format

    Args:
        xml (str): the path to the xml file
        img (str): the path to the image file (jpg)
        destination_folder (Path): destination folder path
        class_mapping (Dict): class mapping from pascal VOC to yolo
        copy (bool): whether to copy from source to destination or move
    """
    # read xml file
    ann = annotation_from_xml(xml)

    # get ann str
    yolo_ann = ann.to_yolo(class_mapping)

    # save yolo format file
    with open(
        (destination_folder / "labels" / Path(xml).name).with_suffix(".txt"),
        "w",
        encoding='UTF-8'
    ) as f:
        f.write(yolo_ann)
        f.close()
    if copy:
        shutil.copy(img, destination_folder / "images" / Path(img).name)
    else:
        shutil.move(img, destination_folder / "images" / Path(img).name)

def remove_ann_classes(
    txt:str,
    class_to_exclude:List
):
    """remove annotation classes from the annotation file

    Args:
        txt (str): path to annotation file (txt)
        class_to_exclude (List): list of classes to remove
    """
    # Read the annotation file, filter lines based on class labels, and write back to the file
    with open(txt, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    with open(txt, 'w', encoding='UTF-8') as file:
        for line in lines:
            # Split the line into components
            parts = line.split()
            if len(parts) > 0:
                class_label = parts[0]
                if class_label not in class_to_exclude:
                    file.write(line)

def class_remap(
    txt:str,
    class_map:Dict
):
    """remap the class

    Args:
        txt (str): path to annotation file (txt)
        class_map (Dict): dictionaty with class mapping
    """
    with open(txt, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    with open(txt, 'w', encoding='UTF-8') as file:
        for line in lines:
            # Split the line into components
            parts = line.split()
            # remap the first class id
            parts[0] = class_map[parts[0]]
            file.write(' '.join(parts)+'\n')
