import matplotlib.pyplot as plt
import numpy as np
import os
import requests
import skimage.io as skio


def save_img(img_links, img_idx, verbose=False):
    """
    Save images from a dictionary of image links to files and optionally display them.
    
    This function iterates through a dictionary of image links where keys are image identifiers 
    and values are URLs. For each image link, it sends a GET request to download the image. 
    If the download is successful (HTTP status code 200), it extracts the image extension from 
    the URL, constructs a save path in the format "img/{img_idx}_{index + 1}_{key}.{img_extension}", 
    and saves the image content to the specified path. If the `verbose` parameter is True, 
    it also displays the downloaded image using matplotlib. If the download fails, it prints 
    a message indicating the failure.
    
    :param img_links: A dictionary of image identifiers and URLs.
    :type img_links: dict
    :param img_idx: Identifier or index for the images being saved.
    :type img_idx: int or str
    :param verbose: Optional boolean to show the downloaded image using matplotlib (default is False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    for idx, key, url in zip(
        range(0, len(img_links)), img_links.keys(), img_links.values()
    ):
        response = requests.get(url)
        if response.status_code == 200:
            img_extension = url.split(".")[-1]
            save_path = os.path.join(
                "img", f"{img_idx}_{idx + 1}_{key}.{img_extension}"
            )
            with open(save_path, "wb") as f:
                f.write(response.content)
            if verbose:
                plt.imshow(np.array(skio.imread(url)), interpolation="nearest")
                plt.show()
        else:
            print(f"Failed to download {key}")
