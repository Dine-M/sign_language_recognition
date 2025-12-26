"""
Real-time Sign Language Detection using YOLOv7
"""

import argparse
import subprocess
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="YOLOv7 Real-Time Detection")
    parser.add_argument("--weights", type=str, default="weights/best.pt")
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--source", type=int, default=0)

    args = parser.parse_args()

    yolov7_detect = Path("yolov7/detect.py")

    if not yolov7_detect.exists():
        sys.exit("YOLOv7 repository not found. Clone it first.")

    command = [
        sys.executable,
        "yolov7/detect.py",
        "--weights", args.weights,
        "--conf", str(args.conf),
        "--source", str(args.source)
    ]

    subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
