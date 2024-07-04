import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from .find_color_range import find_color_range
from .convert_to_numerical_tuple import convert_to_numerical_tuple
from .manual_fix import manual_fix


def extract(np_img, key, img_idx, extraction_name, param, fix=None, verbose=False):
    """
    Extract and Concatenate Image Regions, Apply HSV Color Mask, and Save the Resulting Image.

    This function extracts specified regions from an image, concatenates them horizontally, and applies
    an HSV color mask based on the color range found in the concatenated image. The resulting image is
    optionally displayed, saved to a file, and returned. Additionally, a specified region of the resulting
    image can be filled with zeros if the `fix` parameter is provided.

    :param np_img: Dictionary where keys are image identifiers and values are numpy arrays representing images.
    :type np_img: dict
    :param key: Key for the image to be processed.
    :type key: str
    :param img_idx: Index of the image to be used for saving the extracted image file.
    :type img_idx: str
    :param extraction_name: Name to be used for saving the extracted image file.
    :type extraction_name: str
    :param param: Dictionary specifying the method and value for extracting color range.
                  The `method` key can be either "sampling" or "exact".
                  - If `method` is "sampling", `param["value"]` should be a list of tuples specifying the regions to be extracted and concatenated.
                    Each tuple should contain four values (start_col, end_col, start_row, end_row), where start_row < end_row and start_col < end_col.
                  - If `method` is "exact", `param["value"]` should be a list of two tuples specifying the minimum and maximum HSV values.
                    Each tuple should contain three values (H, S, V).
    :type param: dict
    :param fix: Tuple specifying the region to be filled with zeros. The tuple should contain four values
                (start_col, end_col, start_row, end_row). Default is None.
    :type fix: tuple or None
    :param verbose: Whether to display intermediate results and print additional information. Default is False.
    :type verbose: bool
    :return: The extracted image with shape as (960, 960, 3).
    :rtype: numpy.ndarray
    """
    img = np_img[key].reshape(960, 960, 3)

    color_range_min = (None, None, None)
    color_range_max = (None, None, None)

    if param["method"] == "sampling":
        # Input validation
        if not (isinstance(param["value"], list) and len(param["value"]) > 0):
            raise ValueError("param['value'] must be a non-empty list of tuples.")
        for region in param["value"]:
            if not (isinstance(region, tuple) and len(region) == 4):
                raise ValueError(
                    "Each item in param['value'] must be a tuple of length 4."
                )
            start_row, end_row, start_col, end_col = region
            if not (start_row < end_row and start_col < end_col):
                raise ValueError(
                    "In each tuple, start_row must be less than end_row and start_col must be less than end_col."
                )

        regions = [
            img[start_col:end_col, start_row:end_row]
            for start_col, end_col, start_row, end_row in param["value"]
        ]
        concatenated_image = cv2.hconcat(regions)

        if verbose:
            print(f"{key} sample region")
            plt.imshow(concatenated_image)
            plt.show()
            plt.close()
            print("\n")

        color_range_min, color_range_max = find_color_range(concatenated_image)
    elif param["method"] == "exact":
        # Input validation
        if not (isinstance(param["value"], list) and len(param["value"]) == 2):
            raise ValueError("param['value'] must be a non-empty list of 2 tuples.")
        for region in param["value"]:
            if not (isinstance(region, tuple) and len(region) == 3):
                raise ValueError(
                    "Each item in param['value'] must be a tuple of length 3."
                )

        color_range_min = param["value"][0]
        color_range_max = param["value"][1]
    else:
        raise ValueError("Incorrect `method`. It must be either 'sampling' or 'exact'.")

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
        print("\n")
    plt.close()

    if isinstance(fix, tuple) and len(fix) == 4:
        extraction = manual_fix(
            extraction, key, img_idx, extraction_name, fix[0], fix[1], fix[2], fix[3], verbose
        )

    return extraction
