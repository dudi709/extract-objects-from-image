# Extract objects from images
This code was written to allow objects to be saved as images from larger images.
The code creates directories of objects under the `output/` directory and saves each image (object) under its corresponding directory.
Object detection is performed by YOLOv3 - object detector.

# The Code

### Prerequisites

```sh
  pip install tensorflow==2.0.0
  pip install keras==2.3.0
  pip install pillow
  ```
Before executing the [main.py](https://github.com/dudi709/extract-objects-from-image/blob/main/main.py) file:
- Place your images under `input/` directory.
- Download pretrained [model](https://drive.google.com/file/d/19XC9ujio7AwpT52tcWiUmaoxoDWdjrQw/view?usp=sharing) file and place it under the `model/` directory.
- You can select the objects you want to cut from the images by changing the default value of the `objects_to_extract` argument found in the [main.py](https://github.com/dudi709/extract-objects-from-image/blob/main/main.py) file.

After running the program you can find your output under the `output/` directory.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Dudi Biton - dudi709@gmail.com
