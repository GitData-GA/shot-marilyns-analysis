import numpy as np
import skimage.io as skio

# Read:
# Takes in a list of file paths (URLs) to images.
#
# Modify:
# Reads each image from the provided file paths using skimage.io.imread.
# Appends each image (as a NumPy array) to a list.
#
# Export:
# Returns a NumPy array containing all the images.
def np_convert(filepaths):
  img_data = []
  for filepath in filepaths:
    img = skio.imread(filepath)
    img_data.append(img)
  return np.array(img_data)
