import numpy as np
from sklearn.cluster import KMeans


def kmeans(
    pd_img,
    red_column="Red",
    green_column="Green",
    blue_column="Blue",
    n_clusters=20,
    random_state=88,
    init="k-means++",
    n_init="auto",
):
    """
    K-means Clustering on Image Data in Pandas DataFrames.

    This function performs K-means clustering on image data stored in Pandas DataFrames
    contained within the dictionary `pd_img`. Each DataFrame should include columns for
    RGB values, which can be customized using parameters `red_column`, `green_column`,
    and `blue_column`. Optional parameters allow specification of clustering settings
    such as `n_clusters`, `random_state`, `init`, and `n_init` for K-means algorithm.

    :param pd_img: Dictionary where keys are image identifiers and values are Pandas DataFrames.
    :type pd_img: dict
    :param red_column: Name of the column representing the red channel (default: "Red").
    :type red_column: str
    :param green_column: Name of the column representing the green channel (default: "Green").
    :type green_column: str
    :param blue_column: Name of the column representing the blue channel (default: "Blue").
    :type blue_column: str
    :param n_clusters: Number of clusters for K-means (default: 20).
    :type n_clusters: int
    :param random_state: Random state for K-means (default: 88).
    :type random_state: int
    :param init: Method for initialization (default: "k-means++").
    :type init: str
    :param n_init: Number of initializations for K-means (default: "auto").
    :type n_init: int or "auto"
    :return: Dictionary where keys are image identifiers and values are fitted K-means models.
    :rtype: dict
    """
    results = {}
    for key, img in pd_img.items():
        results[key] = KMeans(
            n_clusters=n_clusters, random_state=random_state, init=init, n_init=n_init
        ).fit(img[[red_column, green_column, blue_column]])
    return results


