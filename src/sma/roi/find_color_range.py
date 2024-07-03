import cv2
import numpy as np


def find_color_range(img):
    """
    Find the HSV Color Range in an Image.

    This function converts an input RGB image to HSV color space and computes the minimum
    and maximum values for the hue, saturation, and value (HSV) channels. It returns a tuple
    of two tuples, representing the minimum and maximum HSV values found in the image.

    :param image: Input image in RGB color space.
    :type image: numpy.ndarray
    :return: A tuple containing two tuples:
             - (h_min, s_min, v_min): Minimum HSV values.
             - (h_max, s_max, v_max): Maximum HSV values.
    :rtype: tuple
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h_min, s_min, v_min = np.min(hsv_img, axis=(0, 1))
    h_max, s_max, v_max = np.max(hsv_img, axis=(0, 1))
    return (h_min, s_min, v_min), (h_max, s_max, v_max)
