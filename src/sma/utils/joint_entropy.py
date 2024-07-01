import numpy as np
from .shanon_entropy import shanon_entropy


def joint_entropy(Y, X):
    """
    Calculate the joint entropy of two input arrays Y and X.

    This function calculates the joint entropy of two input arrays Y and X. It
    concatenates Y and X along columns using `np.c_` to create a new array YX. It
    calls the `shanon_entropy` function to calculate the entropy of the combined
    array YX.

    :param Y: A NumPy array.
    :type Y: numpy.ndarray
    :param X: A NumPy array.
    :type X: numpy.ndarray
    :return: The joint entropy of Y and X as a scalar value.
    :rtype: float
    """
    YX = np.c_[Y, X]
    return shanon_entropy(YX)
