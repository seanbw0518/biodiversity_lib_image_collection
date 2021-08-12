import PIL
from skimage import color, filters
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import label2rgb
from PIL import Image
from scipy import ndimage as ndi
from skimage.measure import regionprops
import os

in_directory = "D:\OneDrive\Documents\Programming\Python\imageDL\High-Res Images (Categorized)\Plants"
out_directory = in_directory + "\\cropped"

uncropped_images = os.listdir(in_directory)
num_of_images = len(uncropped_images)

i = 0
for uncropped_image in uncropped_images:

    perct_prog = round((i / num_of_images) * 100, 3)
    print("PROGRESS: " + str(perct_prog) + "%, REMAINING: " + str(num_of_images - i - 1))

    print("Processing image: " + uncropped_image + "...")
    # get image
    try:
        image = Image.open(in_directory + "\\" + uncropped_image)
    except PermissionError as pe:
        continue
    except PIL.UnidentifiedImageError as uie:
        os.remove(in_directory + "\\" + uncropped_image)
        print("File error, DELETED")
        continue

    # get size of image & shrink it for quicker processing
    w = image.size[0]
    h = image.size[1]
    scale_factor = 0.3
    new_w = round(w * scale_factor)
    new_h = round(h * scale_factor)
    image_small = image.resize((new_w, new_h))
    img = np.array(image_small)

    # convert to grayscale
    image_gray = color.rgb2gray(img)
    """ plt.imsave("gray.png", image_gray) """

    # apply triangle mask to make binary
    triangle = filters.threshold_triangle(image_gray)
    tri_mask = image_gray < triangle
    """ plt.imsave("mask.png", tri_mask) """

    # clean binary image
    label_objects, nb_labels = ndi.label(tri_mask)
    sizes = np.bincount(label_objects.ravel())
    mask_sizes = sizes > 2
    mask_sizes[0] = 0
    cleaned_mask = mask_sizes[label_objects]

    tri_fill = ndi.binary_fill_holes(cleaned_mask)
    """ plt.imsave("fill.png", tri_fill) """

    label_objects, nb_labels = ndi.label(tri_fill)
    sizes = np.bincount(label_objects.ravel())
    mask_sizes = sizes > 150
    mask_sizes[0] = 0
    cleaned_fill = mask_sizes[label_objects]

    """ plt.imsave("cleaned.png", cleaned_fill) """

    # create segmentation
    labeled_objects, _ = ndi.label(cleaned_fill)
    image_label_overlay = label2rgb(labeled_objects, image=image_gray, bg_label=0)
    """ plt.imsave("overlay.png", image_label_overlay) """
    """ plt.imsave("seg.png", labeled_objects) """

    j = 0
    for region in regionprops(labeled_objects):
        print("--> cropping: " + str(j))

        # get bounds around segmented objects
        y1, x1, y2, x2 = region.bbox

        y1_big = round(y1 / scale_factor)
        x1_big = round(x1 / scale_factor)
        y2_big = round(y2 / scale_factor)
        x2_big = round(x2 / scale_factor)

        try:
            cropped = np.array(image)[y1_big - 5:y2_big + 5, x1_big - 5:x2_big + 5]
            imgc = np.array(cropped)

            plt.imsave(out_directory + "\\" + uncropped_image[:-4] + " - crop" + str(j) + ".jpg", imgc)
        except SystemError:
            cropped = np.array(image)[y1_big:y2_big, x1_big:x2_big]

            imgc = np.array(cropped)

            plt.imsave(out_directory + "\\" + uncropped_image[:-4] + " - crop" + str(j) + ".jpg", imgc)

        j += 1

    i += 1
