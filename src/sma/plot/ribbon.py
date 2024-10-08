import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def ribbon(
    pd_img,
    img_idx,
    kmeans,
    width=10,
    height=0.3,
    output_format="pdf",
    verbose=False,
):
    """
    Generate and save horizontal bar charts representing cluster distributions for images using K-means clustering.

    This function takes a dictionary `pd_img` where keys are image identifiers and values are Pandas DataFrames containing image data.
    It requires an integer `img_idx` indicating the index of the image to plot and a dictionary `kmeans` where keys match those in `pd_img`
    and values are fitted KMeans objects. Optional parameters include `width` for plot width (default: 10), `height` for plot height (default: 0.65),
    `output_format` for saving plot file format (default: 'pdf'), and `verbose` to display the plot (default: False).

    :param pd_img: Dictionary with image identifiers as keys and Pandas DataFrames containing image data as values.
    :type pd_img: dict
    :param img_idx: Integer index indicating which image to plot.
    :type img_idx: int
    :param kmeans: Dictionary with the same keys as `pd_img` and values as fitted KMeans objects.
    :type kmeans: dict
    :param width: Width of the plot (default: 10).
    :type width: float
    :param height: Height of the plot (default: 0.3).
    :type height: float
    :param output_format: File format for saving plots (default: 'pdf').
    :type output_format: str
    :param verbose: Boolean to control whether to display the plot (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    plt.rcParams["font.family"] = "STIXGeneral"
    idx = 0
    for key, img in pd_img.items():
        if isinstance(kmeans, dict):
            if isinstance(kmeans[key], KMeans) and (pd_img.keys() == kmeans.keys()):
                kmeans_result = kmeans[key]

                cluster_counts = np.bincount(kmeans_result.labels_)
                cluster_colors = kmeans_result.cluster_centers_ / 255

                sorted_indices = np.argsort(cluster_counts)[::-1]
                sorted_counts = cluster_counts[sorted_indices]
                sorted_colors = cluster_colors[sorted_indices]

                fig, ax = plt.subplots(figsize=(width, height))
                sorted_counts_normalized = sorted_counts / sorted_counts.sum()
                sorted_colors_hex = [
                    f"#{int(color[0]*255):02x}{int(color[1]*255):02x}{int(color[2]*255):02x}"
                    for color in sorted_colors
                ]

                # Identify the dominant color
                dominant_color_index = 0
                dominant_color_rgb = sorted_colors[dominant_color_index]
                dominant_color_rgb_text = f"({int(dominant_color_rgb[0]*255)}, {int(dominant_color_rgb[1]*255)}, {int(dominant_color_rgb[2]*255)})"

                for i, (color, segment_width) in enumerate(
                    zip(sorted_colors_hex, sorted_counts_normalized)
                ):
                    ax.barh(
                        0,
                        segment_width,
                        left=np.sum(sorted_counts_normalized[:i]),
                        color=color,
                        edgecolor="none",
                    )

                ax.set_xlim(0, 1)
                ax.set_yticks([])
                ax.set_xticks([])
                ax.axis("off")
                fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

                # Add the bracket under the dominant color
                dominant_width = sorted_counts_normalized[dominant_color_index]
                left_pos = np.sum(sorted_counts_normalized[:dominant_color_index])

                # Draw a large bracket under the dominant color
                bracket_y = -0.5
                ax.annotate(
                    "",
                    xy=(left_pos, bracket_y),
                    xytext=(left_pos + dominant_width, bracket_y),
                    arrowprops=dict(
                        arrowstyle="|-|",
                        lw=0.75,
                        shrinkA=0.5,
                        shrinkB=0.5,
                        mutation_scale=3.75,
                    ),
                    annotation_clip=False,
                )

                # Text for RGB value (remove annotation_clip)
                ax.text(
                    left_pos + dominant_width / 2,
                    bracket_y - 0.05,
                    dominant_color_rgb_text,
                    ha="center",
                    va="top",
                    fontsize=9,
                    color="black",
                )

                # Save the plot
                plt.savefig(
                    f"img/{img_idx}_{idx + 1}_{key}_color_ribbon.{output_format}",
                    format=output_format,
                    bbox_inches="tight",
                    dpi=512,
                    pad_inches=0,
                )

                if verbose:
                    print(f"{key} color ribbon")
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
