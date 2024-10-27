from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def knn_repair(
    np_img,
    key,
    img_idx,
    n_neighbors,
    start_col,
    end_col,
    start_row,
    end_row,
    damaged_pixel=None,
    verbose=False,
):
    """
    Repair Damaged Sections of an Image Using K-Nearest Neighbors (KNN) Regression.

    This function repairs a specified damaged section of an image using KNN regression. The repaired image is optionally displayed,
    saved to a file, and returned.

    :param np_img: Dictionary where keys are image identifiers and values are numpy arrays representing images.
    :type np_img: dict
    :param key: Key for the image to be processed.
    :type key: str
    :param img_idx: Index of the image to be used for saving the repaired image file.
    :type img_idx: str
    :param n_neighbors: Number of neighbors to use for KNN regression.
    :type n_neighbors: int
    :param start_col: The starting column index for the damaged region to be repaired.
    :type start_col: int
    :param end_col: The ending column index for the damaged region to be repaired.
    :type end_col: int
    :param start_row: The starting row index for the damaged region to be repaired.
    :type start_row: int
    :param end_row: The ending row index for the damaged region to be repaired.
    :type end_row: int
    :param verbose: Whether to display the repaired image and print additional information. Default is False.
    :type verbose: bool
    :return: The repaired image.
    :rtype: numpy.ndarray
    :raises ValueError: If start_row is not less than end_row or start_col is not less than end_col.
    """
    plt.rcParams['font.family'] = 'STIXGeneral'
    if start_col >= end_col or start_row >= end_row:
        raise ValueError(
            "start_row must be less than end_row and start_col must be less than end_col."
        )

    img = np_img[key].reshape(960, 960, 3)
    damaged_section = img[start_col:end_col, start_row:end_row]

    mask = np.zeros((960, 960), dtype=bool)
    mask[start_col:end_col, start_row:end_row] = True

    undamaged_pixels = img[~mask].reshape(-1, 3)
    damaged_coords = np.column_stack(np.where(mask))
    undamaged_coords = np.column_stack(np.where(~mask))

    knn = KNeighborsRegressor(n_neighbors=n_neighbors)
    knn.fit(undamaged_coords, undamaged_pixels)

    predicted_pixels = knn.predict(damaged_coords)

    if damaged_pixel is not None:
        distances, indices = knn.kneighbors([damaged_pixel])
        nearest_neighbor_colors = undamaged_pixels[indices[0]]
        print(nearest_neighbor_colors)
        print(distances, indices)

    repaired_img = deepcopy(img)
    for (i, j), pixel in zip(damaged_coords, predicted_pixels):
        repaired_img[i, j] = pixel

    plt.imshow(repaired_img)
    plt.axis("off")

    plt.savefig(
        f"img/{img_idx}_{key}_repair.jpg",
        format="jpg",
        dpi=512,
        bbox_inches="tight",
        pad_inches=0,
    )

    if verbose:
        print(f"KNN Regressor detail:\n {knn}")
        print(f"{key} repair")
        plt.show()
        print("\n")
    plt.close()

    return repaired_img.reshape(-1, 3)
