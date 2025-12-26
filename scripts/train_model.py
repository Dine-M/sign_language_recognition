"""
Train YOLOv7 model for Sign Language Recognition
"""

import argparse
import subprocess
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="YOLOv7 Training")
    parser.add_argument("--img", type=int, default=640)
    parser.add_argument("--batch", type=int, default=4)
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--data", type=str, default="data/custom.yaml")
    parser.add_argument("--weights", type=str, default="yolov7.pt")

    args = parser.parse_args()

    yolov7_train = Path("yolov7/train.py")

    if not yolov7_train.exists():
        sys.exit("YOLOv7 repository not found. Clone it first.")

    command = [
        sys.executable,
        "yolov7/train.py",
        "--img", str(args.img),
        "--batch", str(args.batch),
        "--epochs", str(args.epochs),
        "--data", args.data,
        "--weights", args.weights
    ]

    subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
