import numpy as np
import skimage.io as skio


def np_convert(img_links):
    """
    Convert images from URLs to a dictionary of NumPy arrays.

    This function takes in a dictionary where keys are image names and values are URLs to images.
    It reads each image from the provided URLs using `skimage.io.imread` and appends each image
    (as a NumPy array) to a dictionary.

    :param img_links: A dictionary where keys are image names and values are URLs to images.
    :type img_links: dict
    :return: A dictionary containing image names as keys and images as NumPy arrays.
    :rtype: dict
    """
    img_data = {}
    for key, url in img_links.items():
        img_data[key] = np.array(skio.imread(url)).reshape(-1, 3)
    return img_data
