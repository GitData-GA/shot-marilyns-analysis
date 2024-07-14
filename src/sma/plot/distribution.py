import matplotlib.pyplot as plt
import numpy as np


def distribution(
    np_img, img_idx, width=6, height=4.5, output_format="pdf", verbose=False
):
    """
    Generate and save distribution plots of RGB channels for images converted to NumPy arrays.

    This function takes a dictionary `np_img` where keys are image identifiers and values are
    NumPy arrays representing images. It requires an integer `img_idx` representing the index
    of the image to be plotted. Optional parameters include `width` and `height` for setting
    plot dimensions, `output_format` for saving the plot file format, and `verbose` to control
    whether to display the plot.

    :param np_img: Dictionary with image identifiers as keys and NumPy arrays representing images as values.
    :type np_img: dict
    :param img_idx: Integer index indicating which image to plot.
    :type img_idx: int
    :param width: Width of the plot (default: 6).
    :type width: float
    :param height: Height of the plot (default: 4.5).
    :type height: float
    :param output_format: File format for saving plots (default: 'svg').
    :type output_format: str
    :param verbose: Boolean to control whether to display the plot (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    for idx, key, img in zip(range(0, len(np_img)), np_img.keys(), np_img.values()):
        red_channel = img[:, 0]
        green_channel = img[:, 1]
        blue_channel = img[:, 2]

        red_hist = np.histogram(red_channel, bins=256, range=(0, 256))[0]
        green_hist = np.histogram(green_channel, bins=256, range=(0, 256))[0]
        blue_hist = np.histogram(blue_channel, bins=256, range=(0, 256))[0]

        total_pixels = img.shape[0] * img.shape[1]
        red_prob = red_hist / total_pixels
        green_prob = green_hist / total_pixels
        blue_prob = blue_hist / total_pixels
        ylim_upper = max(max(red_prob), max(green_prob), max(blue_prob))

        plt.figure(figsize=(width, height))
        plt.plot(red_prob, color="red")
        plt.plot(green_prob, color="green")
        plt.plot(blue_prob, color="blue")
        plt.xlabel("Channel")
        plt.ylabel("Probability")
        plt.ylim(0, 1.1 * ylim_upper)

        plt.savefig(
            f"img/{img_idx}_{idx + 1}_{key}_dist.{output_format}",
            format=output_format,
            dpi=512,
            bbox_inches="tight",
        )

        if verbose:
            print(f"{key}")
            plt.show()
            print("\n")

        plt.close()
