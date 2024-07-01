import numpy as np
from .rgb_to_hex import rgb_to_hex


def rgb_to_hex_vectorized(rgb_array):
    """
    Convert a NumPy array of RGB tuples to a NumPy array of hexadecimal color codes.

    This function takes in a NumPy array of RGB tuples where each row is an RGB value with 
    three integer values (each ranging from 0 to 255). It applies the `rgb_to_hex` function to 
    each row of the NumPy array using `np.apply_along_axis`. Each RGB value in the array is 
    converted to its corresponding hexadecimal string.

    :param rgb_array: A NumPy array of RGB tuples.
    :type rgb_array: numpy.ndarray
    :return: A NumPy array of strings where each string is a hexadecimal color code.
    :rtype: numpy.ndarray
    """
    return np.apply_along_axis(rgb_to_hex, 1, rgb_array)
