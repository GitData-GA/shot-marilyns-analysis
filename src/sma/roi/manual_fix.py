import numpy as np
import matplotlib.pyplot as plt


def manual_fix(extracted_img, key, img_idx, extraction_name, start_col, end_col, start_row, end_row, verbose=False):
    """
    Fill a Specified Region of an Image with Zeros and Save the Result.

    This function takes an extracted image and fills the specified region with zeros. The modified image is then saved
    as a file and optionally displayed.

    :param extracted_img: The image from which a region will be filled with zeros.
    :type extracted_img: numpy.ndarray
    :param key: Key for the image to be processed.
    :type key: str
    :param img_idx: Index of the image to be used for saving the modified image file.
    :type img_idx: str
    :param extraction_name: Name to be used for saving the modified image file.
    :type extraction_name: str
    :param start_col: The starting column index for the region to be filled.
    :type start_col: int
    :param end_col: The ending column index for the region to be filled.
    :type end_col: int
    :param start_row: The starting row index for the region to be filled.
    :type start_row: int
    :param end_row: The ending row index for the region to be filled.
    :type end_row: int
    :param verbose: Whether to display the modified image and print additional information. Default is False.
    :type verbose: bool
    :return: The image with the specified region filled with zeros.
    :rtype: numpy.ndarray
    """
    if start_col >= end_col or start_row >= end_row:
        raise ValueError("start_row must be less than end_row and start_col must be less than end_col.")
        
    extracted_img[start_col:end_col, start_row:end_row] = np.zeros(
        (end_col - start_col, end_row - start_row, 3), dtype=np.uint8
    )

    plt.imshow(extracted_img)
    plt.axis("off")

    plt.savefig(
        f"img/{img_idx}_{key}_{extraction_name}_extraction.jpg",
        format="jpg",
        dpi=512,
        bbox_inches="tight",
        pad_inches=0,
    )

    if verbose:
        print(f"{key} {extraction_name} fix result")
        plt.show()
        print("\n")
    plt.close()
    
    return extracted_img
