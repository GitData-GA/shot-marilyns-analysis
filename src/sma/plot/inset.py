import matplotlib.pyplot as plt
import numpy as np
import skimage.io as skio

def inset(
    img_path,
    img_idx,
    start_col,
    end_col,
    start_row,
    end_row,
    position,
    hide_axes=True,
    verbose=False,
):
    """
    Display an image with a zoomed-in inset region and save it as a PDF.

    This function reads an image from the specified path, creates a main plot with the image, 
    and overlays an inset (zoomed-in) section of the image. The inset is defined by the row and column limits 
    provided as parameters. The function can optionally hide axes from both the main and inset images, 
    and also allows for visualizing the output during execution. Finally, it saves the image with the inset 
    to a PDF file.

    :param img_path: Path to the image file to be loaded and displayed.
    :type img_path: str
    :param img_idx: Integer index used to name the saved PDF file.
    :type img_idx: int
    :param start_col: Starting column for the zoomed-in inset section.
    :type start_col: int
    :param end_col: Ending column for the zoomed-in inset section.
    :type end_col: int
    :param start_row: Starting row for the zoomed-in inset section.
    :type start_row: int
    :param end_row: Ending row for the zoomed-in inset section.
    :type end_row: int
    :param position: The position of the inset on the main plot, provided as a list of [x, y, width, height].
    :type position: list of float
    :param hide_axes: Optional boolean flag to hide the axes of the inset and main image (default: True).
    :type hide_axes: bool
    :param verbose: Optional boolean flag to display the plot during execution (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    image = skio.imread(img_path)
    fig, ax = plt.subplots()
    ax.imshow(image, interpolation="nearest")
    axins = ax.inset_axes(
        position, xlim=(start_row, end_row), ylim=(start_col, end_col)
    )
    axins.imshow(image)

    if hide_axes:
        axins.set_xticks([])
        axins.set_yticks([])
        ax.set_axis_off()

    ax.indicate_inset_zoom(axins, edgecolor="black")

    plt.savefig(
        f"img/{img_idx}_inset.pdf",
        format="pdf",
        dpi=512,
        bbox_inches="tight",
    )

    if verbose:
        plt.show()

    plt.close()
