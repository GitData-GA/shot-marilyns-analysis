import matplotlib.pyplot as plt
import numpy as np
from sma.utils.relative_conditional_entropy import relative_conditional_entropy


def entropy_heatmap(
    np_img, img_idx, width=6.585, height=6.195, output_format="pdf", verbose=False
):
    """
    Generate and save a heatmap of relative conditional entropy between RGB channels for images converted to NumPy arrays.

    This function takes a dictionary `np_img` where keys are image identifiers and values are NumPy arrays representing images
    converted from URLs. It requires an integer `img_idx` representing the index of the image to be plotted. Optional parameters
    include `width` and `height` for setting plot dimensions, `output_format` for specifying the file format for saving the plot,
    and `verbose` to control whether to display the plot.

    :param np_img: Dictionary with image identifiers as keys and NumPy arrays representing images as values.
    :type np_img: dict
    :param img_idx: Integer index indicating which image to plot.
    :type img_idx: int
    :param width: Width of the plot (default: 6.585).
    :type width: float
    :param height: Height of the plot (default: 6.195).
    :type height: float
    :param output_format: File format for saving plots (default: 'pdf').
    :type output_format: str
    :param verbose: Boolean to control whether to display the plot (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    for idx, key, img in zip(range(0, len(np_img)), np_img.keys(), np_img.values()):
        red = np.hstack(
            (
                img[:, 0].reshape(-1, 1),
                np.zeros((img[:, 0].reshape(-1, 1).shape[0], 1)),
                np.zeros((img[:, 0].reshape(-1, 1).shape[0], 1)),
            )
        )
        green = np.hstack(
            (
                np.zeros((img[:, 1].reshape(-1, 1).shape[0], 1)),
                img[:, 1].reshape(-1, 1),
                np.zeros((img[:, 1].reshape(-1, 1).shape[0], 1)),
            )
        )
        blue = np.hstack(
            (
                np.zeros((img[:, 2].reshape(-1, 1).shape[0], 1)),
                np.zeros((img[:, 2].reshape(-1, 1).shape[0], 1)),
                img[:, 2].reshape(-1, 1),
            )
        )

        red_blue = relative_conditional_entropy(red, blue)
        red_green = relative_conditional_entropy(red, green)
        red_red = relative_conditional_entropy(red, red)
        blue_red = relative_conditional_entropy(blue, red)
        blue_green = relative_conditional_entropy(blue, green)
        blue_blue = relative_conditional_entropy(blue, blue)
        green_blue = relative_conditional_entropy(green, blue)
        green_red = relative_conditional_entropy(green, red)
        green_green = relative_conditional_entropy(green, green)

        probabilities = np.array(
            [
                [red_red, round(red_green, 3), round(red_blue, 3)],
                [round(green_red, 3), green_green, round(green_blue, 3)],
                [round(blue_red, 3), round(blue_green, 3), blue_blue],
            ]
        )

        fig, ax = plt.subplots(figsize=(width, height))

        heatmap = ax.imshow(probabilities, cmap="Reds", vmin=0, vmax=1)

        ax.set_xticks(np.arange(3))
        ax.set_yticks(np.arange(3))
        ax.set_xticklabels(["red", "green", "blue"])
        ax.set_yticklabels(["red", "green", "blue"])

        for i in range(3):
            for j in range(3):
                text = ax.text(
                    j, i, probabilities[i, j], ha="center", va="center", color="black"
                )

        plt.savefig(
            f"img/{img_idx}_{idx + 1}_{key}_entropy.{output_format}",
            format=output_format,
            dpi=512,
            bbox_inches="tight",
        )

        if verbose:
            print(f"{key}")
            plt.show()
            print("\n")

        plt.close()
