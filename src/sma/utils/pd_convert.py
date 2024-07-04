import numpy as np
import pandas as pd
from .np_convert import np_convert
from .rgb_to_hex_vectorized import rgb_to_hex_vectorized


def pd_convert(np_img):
    """
    Convert images from URLs to a dictionary of Pandas DataFrames with RGB and hex values.

    This function takes in a dictionary where keys are image names and values are URLs to images.
    It reads each image from the provided URLs using `np_convert`. For each image, it reshapes
    the image to ensure it has an RGB structure (-1, 3), converts each RGB triplet to a hex color
    code, and combines the RGB values and hex codes into a DataFrame with columns "Red", "Green",
    "Blue", and "hex". The RGB columns are ensured to be of integer type. The DataFrame for each
    image is then appended to a dictionary.

    :param img_links: A dictionary where keys are image names and values are URLs to images.
    :type img_links: dict
    :return: A dictionary of Pandas DataFrames, each containing RGB values and their corresponding hex codes.
    :rtype: dict
    """
    img_data = {}
    for key, img in zip(np_img.keys(), np_img.values()):
        df = pd.DataFrame(
            np.hstack((img, rgb_to_hex_vectorized(img).reshape(-1, 1))),
            columns=["Red", "Green", "Blue", "hex"],
        )
        df[["Red", "Green", "Blue"]] = df[["Red", "Green", "Blue"]].astype(int)
        df[["hex"]] = df[["hex"]].astype(str)
        img_data[key] = df
    return img_data
