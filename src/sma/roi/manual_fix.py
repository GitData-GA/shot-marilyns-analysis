import numpy as np


def manual_fix(extracted_img, start_col, end_col, start_row, end_row):
    """
    Fill a Specified Region of an Image with Zeros.

    This function takes an extracted image and fills the specified region with zeros.

    :param extracted_img: The image from which a region will be filled with zeros.
    :type extracted_img: numpy.ndarray
    :param start_col: The starting column index for the region to be filled.
    :type start_col: int
    :param end_col: The ending column index for the region to be filled.
    :type end_col: int
    :param start_row: The starting row index for the region to be filled.
    :type start_row: int
    :param end_row: The ending row index for the region to be filled.
    :type end_row: int
    :return: The image with the specified region filled with zeros.
    :rtype: numpy.ndarray
    """
    extracted_img[start_col:end_col, start_row:end_row] = np.zeros(
        (end_col - start_col, end_row - start_row, 3), dtype=np.uint8
    )
    return extracted_img
