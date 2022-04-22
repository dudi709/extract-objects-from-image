import os

from keras.models import load_model
from YOLOv3 import load_image_pixels_and_normalize, predict
from PIL import Image


def crop_object(img_path, object_location):
    # Opens a image in RGB mode
    im = Image.open(img_path)

    # Setting the points for cropped image
    left = object_location[0].xmin
    top = object_location[0].ymin
    right = object_location[0].xmax
    bottom = object_location[0].ymax

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    return im1


def extractor(args):
    model = load_model(f"model/{args.model_name}.h5")

    for img in os.listdir(os.path.join(args.images_dir)):
        if img.endswith(args.image_format):

            image, width, height = load_image_pixels_and_normalize(f"{args.images_dir}/{img}", (416, 416))
            v_boxes, v_labels, v_scores = predict(model, image, width, height)
            print(f"Objects identified in '{img}' are: {v_labels}")

            for i, label in enumerate(v_labels):
                if label in args.objects_to_extract:
                    label_path = os.path.join(args.output_dir, label)

                    if not os.path.exists(label_path):
                        os.mkdir(label_path)

                    img_path = os.path.join(args.images_dir, img)
                    cropped_obj = crop_object(img_path, [v_boxes[i]])

                    cropped_obj.save(f"{label_path}/{img[0: img.index('.')]}-{i}.png", "png")
