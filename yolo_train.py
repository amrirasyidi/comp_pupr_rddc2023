"""
_summary_
"""
import os
from pathlib import Path

from ultralytics import YOLO

def main():
    root_dir = Path(os.getcwd())
    data_dir = root_dir / "data"
    yaml_dir = data_dir / "rddc2020_use_pascal / rddc2020_use_pascal_data.yaml"

    # Load a model
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(
        data=yaml_dir,
        epochs=30,
        batch=8,
        patience=10
    )  # train the model

if __name__ == "__main__":
    main()
