import os
import argparse

from objects_extractor import extractor

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--images_dir', type=str,
                        choices=['input'],
                        default='input')

    parser.add_argument('--output_dir', type=str,
                        choices=['output'],
                        default='output')

    parser.add_argument('--model_name', type=str,
                        choices=['yolo_model'],
                        default='yolo_model')

    parser.add_argument('--image_format', type=tuple,
                        choices=[('png', 'jpeg', 'jpg')],
                        default=('png', 'jpeg', 'jpg'))

    # Change the default value to set the objects you want to extract from the image
    parser.add_argument('--objects_to_extract', type=list,
                        choices=[["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
                                  "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
                                  "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
                                  "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
                                  "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
                                  "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl",
                                  "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
                                  "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet",
                                  "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave",
                                  "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                                  "teddy bear", "hair drier", "toothbrush"]],
                        default=["person", "car", "stop sign"])

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    extractor(args)
