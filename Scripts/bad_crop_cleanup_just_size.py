import os
import PIL
from PIL import Image
import numpy as np
import cv2

in_directory = "D:\OneDrive\Documents\Programming\Python\Biodiversity Library Images\Images\Whales & Dolphins"

crops = os.listdir(in_directory)
num_of_images = len(crops)

i = 0
for crop in crops:
    perct_prog = round((i / num_of_images) * 100, 3)
    print("PROGRESS: " + str(perct_prog) + "%, REMAINING: " + str(num_of_images - i - 1))

    print("Processing image: " + crop + "...\n")

    try:
        pil_image = Image.open(in_directory + "\\" + crop)
        image = np.array(pil_image)
        # Convert RGB to BGR
        image_bgr = image[:, :, ::-1].copy()
        image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    except PermissionError as pe:
        continue
    except PIL.UnidentifiedImageError as uie:
        os.remove(in_directory + "\\" + crop)
        print("\n --- DELETED: File Error")
        continue

    w = pil_image.size[0]
    h = pil_image.size[1]
    size = os.path.getsize(in_directory + "\\" + crop)

    if w * h < 75000 or size < 140000:
        pil_image.close()
        os.remove(in_directory + "\\" + crop)
        print(crop + "\n --- DELETED: Too Small")
    i += 1
