import numpy as np
import pandas as pd
from .rgb_to_hex_vectorized import rgb_to_hex_vectorized


def pd_convert(np_img):
    """
    Convert Numpy Image Arrays to a Dictionary of Pandas DataFrames with RGB and Hex Values.

    This function takes in a dictionary where keys are image names and values are numpy arrays representing images.
    For each image, it reshapes the image to ensure it has an RGB structure (-1, 3), converts each RGB triplet to a hex color
    code, and combines the RGB values and hex codes into a DataFrame with columns "Red", "Green", "Blue", and "hex".
    The RGB columns are ensured to be of integer type. The DataFrame for each image is then appended to a dictionary.

    :param np_img: A dictionary where keys are image names and values are numpy arrays representing images.
    :type np_img: dict
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
