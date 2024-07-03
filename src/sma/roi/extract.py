import cv2
import numpy as np
import matplotlib.pyplot as plt
from .find_color_range import find_color_range
from .convert_to_numerical_tuple import convert_to_numerical_tuple


def extract(np_img, key, img_idx, extraction_name, sample_region, verbose=False):
    """
    Extract and Concatenate Image Regions, Apply HSV Color Mask, and Save the Resulting Image.

    This function extracts specified regions from an image, concatenates them horizontally, and applies
    an HSV color mask based on the color range found in the concatenated image. The resulting image is
    optionally displayed, saved to a file, and returned.

    :param np_img: Dictionary where keys are image identifiers and values are numpy arrays representing images.
    :type np_img: dict
    :param key: Key for the image to be processed.
    :type key: str
    :param img_idx: Index of the image to be used for saving the extracted image file.
    :type img_idx: str
    :param extraction_name: Name to be used for saving the extracted image file.
    :type extraction_name: str
    :param sample_region: List of tuples specifying the regions to be extracted and concatenated.
                          Each tuple should contain four values (start_row, end_row, start_col, end_col),
                          where start_row < end_row and start_col < end_col.
    :type sample_region: list of tuples
    :param verbose: Whether to display intermediate results and print additional information. Default is False.
    :type verbose: bool
    :return: The extracted image with shape as (960, 960, 3).
    :rtype: numpy.ndarray
    """
    # Input validation for sample_region
    if not (isinstance(sample_region, list) and len(sample_region) > 0):
        raise ValueError("sample_region must be a non-empty list of tuples.")
    for region in sample_region:
        if not (isinstance(region, tuple) and len(region) == 4):
            raise ValueError("Each item in sample_region must be a tuple of length 4.")
        start_row, end_row, start_col, end_col = region
        if not (start_row < end_row and start_col < end_col):
            raise ValueError(
                "In each tuple, start_row must be less than end_row and start_col must be less than end_col."
            )

    img = np_img[key].reshape(960, 960, 3)
    regions = [
        img[start_row:end_row, start_col:end_col]
        for start_row, end_row, start_col, end_col in sample_region
    ]
    concatenated_image = cv2.hconcat(regions)

    if verbose:
        print(f"{key} sample region")
        plt.imshow(concatenated_image)
        plt.show()
        plt.close()
        print("\n")

    color_range_min, color_range_max = find_color_range(cropped_image)
    h_min, s_min, v_min = color_range_min
    h_max, s_max, v_max = color_range_max

    if verbose:
        print(f"Color Range (Min): H={h_min}, S={s_min}, V={v_min}")
        print(f"Color Range (Max): H={h_max}, S={s_max}, V={v_max}")
        print("\n")

    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    color_range_min = convert_to_numerical_tuple(color_range_min)
    color_range_max = convert_to_numerical_tuple(color_range_max)

    lo_square = np.full((10, 10, 3), color_range_min, dtype=np.uint8) / 255.0
    do_square = np.full((10, 10, 3), color_range_max, dtype=np.uint8) / 255.0

    mask = cv2.inRange(hsv_img, color_range_min, color_range_max)
    extraction = cv2.bitwise_and(img, img, mask=mask)

    plt.imshow(extraction)
    plt.axis("off")

    plt.savefig(
        f"img/{img_idx}_{key}_{extraction_name}_extraction.jpg",
        format="jpg",
        dpi=512,
        bbox_inches="tight",
        pad_inches=0,
    )

    if verbose:
        print(f"{key} {extraction_name} extraction result")
        plt.show()
        plt.close()
        print("\n")

    return extraction
