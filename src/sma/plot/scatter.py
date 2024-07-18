import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.cluster import KMeans


def scatter(
    pd_img,
    img_idx,
    kmeans=None,
    angles=[(30, 45), (30, 135), (30, 225), (30, 315)],
    width=5,
    height=5,
    output_format="jpg",
    verbose=False,
):
    """
    Generate and save 3D scatter plots for images with optional K-means clustering.

    This function takes a dictionary `pd_img` where keys are image identifiers and values are Pandas DataFrames containing image data.
    It requires an integer `img_idx` indicating the index of the image to plot. It optionally accepts a dictionary `kmeans` (default: None)
    containing KMeans objects with keys matching those in `pd_img` for performing clustering. Additional optional parameters include `angles`,
    a list of tuples specifying (elevation, azimuth) angles for 3D scatter plots (default: [(30, 45), (30, 135), (30, 225), (30, 315)]),
    `width` and `height` for plot dimensions (default: width=5, height=5), `output_format` for saving plot file format (default: 'jpg'),
    and `verbose` to control display of plots (default: False).

    :param pd_img: Dictionary with image identifiers as keys and Pandas DataFrames containing image data as values.
    :type pd_img: dict
    :param img_idx: Integer index indicating which image to plot.
    :type img_idx: int
    :param kmeans: Optional dictionary with keys matching `pd_img` and values as fitted KMeans objects for clustering (default: None).
    :type kmeans: dict or None
    :param angles: Optional list of tuples specifying (elevation, azimuth) angles for 3D scatter plots (default: [(30, 45), (30, 135), (30, 225), (30, 315)]).
    :type angles: list of tuple
    :param width: Width of the plot (default: 5).
    :type width: float
    :param height: Height of the plot (default: 5).
    :type height: float
    :param output_format: File format for saving plots (default: 'jpg').
    :type output_format: str
    :param verbose: Boolean to control whether to display the plot (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    idx = 0
    for key, img in zip(pd_img.keys(), pd_img.values()):
        if (kmeans is not None) and (isinstance(kmeans, dict)):
            if isinstance(kmeans[key], KMeans) and (pd_img.keys() == kmeans.keys()):
                kmeans_result = kmeans[key]
                for angle in angles:
                    fig = plt.figure(figsize=(width, height))
                    ax = fig.add_subplot(111, projection="3d")

                    ax.set_xlabel("Red")
                    ax.set_ylabel("Green")
                    ax.set_zlabel("Blue")

                    for i in range(kmeans_result.n_clusters):
                        cluster_points = img[kmeans_result.labels_ == i]
                        centroid_color = (
                            np.round(kmeans_result.cluster_centers_).astype(int)[i]
                            / 255
                        )
                        ax.scatter(
                            cluster_points["Red"],
                            cluster_points["Green"],
                            cluster_points["Blue"],
                            color=centroid_color,
                            s=5,
                        )

                    ax.set_box_aspect(None, zoom=0.9)
                    ax.view_init(elev=angle[0], azim=angle[1])

                    plt.savefig(
                        f"img/{img_idx}_{idx + 1}_{key}_cluster_scatter.{output_format}",
                        format=output_format,
                        dpi=512,
                        bbox_inches="tight",
                    )

                    if verbose:
                        print(f"{key}, elev={angle[0]}, azim={angle[1]}")
                        plt.show()
                        print("\n")

                    plt.close()
                    idx += 1
            else:
                print(
                    "Argument 'kmeans' is not correct. It must be a `dict` with KMeans objects. Also the keys of the dictionary must be the same as the `pd_img` dictionary."
                )
        elif kmeans is None:
            for angle in angles:
                fig = plt.figure(figsize=(width, height))
                ax = fig.add_subplot(111, projection="3d")

                ax.set_xlabel("Red")
                ax.set_ylabel("Green")
                ax.set_zlabel("Blue")

                ax.scatter(img["Red"], img["Green"], img["Blue"], color=img["hex"], s=5)

                ax.set_box_aspect(None, zoom=0.9)
                ax.view_init(elev=angle[0], azim=angle[1])

                plt.savefig(
                    f"img/{img_idx}_{idx + 1}_{key}_original_scatter.{output_format}",
                    format=output_format,
                    dpi=512,
                    bbox_inches="tight",
                )

                if verbose:
                    print(f"{key}, elev={angle[0]}, azim={angle[1]}")
                    plt.show()
                    print("\n")

                plt.close()
                idx += 1
        else:
            print(
                "Argument 'kmeans' is not correct. It must be `None` or a `dict` with KMeans objects."
            )
