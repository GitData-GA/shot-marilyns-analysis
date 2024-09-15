import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def bar(
    pd_img,
    img_idx,
    kmeans,
    width=5,
    height=3.5,
    output_format="pdf",
    verbose=False,
):
    """
    Generate and save a bar chart of clustered colors for an image.

    This function takes a dictionary `pd_img` where keys are image identifiers and values are
    Pandas DataFrames containing image data. It requires an integer `img_idx` indicating the
    index of the image to plot. Additionally, it expects a dictionary `kmeans` where keys are
    the same as `pd_img` and values are fitted KMeans models. Optional parameters include `width`
    and `height` for the plot dimensions, `output_format` for saving the plot, and `verbose`
    to control whether to display the plot.

    :param pd_img: Dictionary with image identifiers as keys and Pandas DataFrames containing image data as values.
    :type pd_img: dict
    :param img_idx: Integer index indicating which image to plot.
    :type img_idx: int
    :param kmeans: Dictionary with the same keys as `pd_img` and values as fitted KMeans models.
    :type kmeans: dict
    :param width: Width of the plot (default: 5).
    :type width: int
    :param height: Height of the plot (default: 3.5).
    :type height: int
    :param output_format: File format for saving plots (default: 'pdf').
    :type output_format: str
    :param verbose: Boolean to control whether to display the plot (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    idx = 0
    for key, img in zip(pd_img.keys(), pd_img.values()):
        if isinstance(kmeans, dict):
            if isinstance(kmeans[key], KMeans) and (pd_img.keys() == kmeans.keys()):
                kmeans_result = kmeans[key]

                plt.figure(figsize=(width, height))
                cluster_counts = np.bincount(kmeans_result.labels_)
                cluster_colors = kmeans_result.cluster_centers_ / 255

                sorted_indices = np.argsort(cluster_counts)[::-1]
                sorted_counts = cluster_counts[sorted_indices]
                sorted_colors = cluster_colors[sorted_indices]

                bar_positions = np.arange(1, kmeans_result.n_clusters + 1)
                plt.bar(bar_positions, sorted_counts, color=sorted_colors)

                plt.xlabel("Cluster Number")
                plt.ylabel("Number of Pixels")
                plt.xticks(bar_positions)

                # Create legend
                rgb_colors = [
                    f"({int(color[0]*255)}, {int(color[1]*255)}, {int(color[2]*255)})"
                    for color in sorted_colors
                ]
                legend_patches = [
                    plt.Rectangle((0, 0), 1, 1, color=sorted_colors[i])
                    for i in range(kmeans_result.n_clusters)
                ]
                legend = plt.legend(
                    legend_patches,
                    rgb_colors,
                    loc="right",
                    bbox_to_anchor=(1.25, 0.5),
                    title="Centroid values\n(red, green, blue)",
                )

                plt.savefig(
                    f"img/{img_idx}_{idx + 1}_{key}_cluster_bar_chart.{output_format}",
                    format=output_format,
                    dpi=512,
                    bbox_inches="tight",
                )

                if verbose:
                    print(f"{key} bar chart")
                    plt.show()
                    print("\n")

                plt.close()
                idx += 1
            else:
                print(
                    "Argument 'kmeans' is not correct. It must be a `dict` with KMeans objects. Also the keys of the dictionary must be the same as the `pd_img` dictionary."
                )
        else:
            print(
                "Argument 'kmeans' is not correct. It must be a `dict` with KMeans objects."
            )
