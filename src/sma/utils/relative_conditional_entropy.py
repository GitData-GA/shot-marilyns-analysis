from .conditional_entropy import conditional_entropy
from .shanon_entropy import shanon_entropy


def relative_conditional_entropy(Y, X):
    """
    Calculate the relative conditional entropy of Y given X.

    This function calculates the relative conditional entropy of Y given X. It
    calls the `conditional_entropy` function to calculate the conditional entropy of
    Y given X. It calls the `shanon_entropy` function to calculate the entropy of Y.
    It divides the conditional entropy by the entropy of Y to get the relative
    conditional entropy.

    :param Y: A NumPy array.
    :type Y: numpy.ndarray
    :param X: A NumPy array.
    :type X: numpy.ndarray
    :return: The relative conditional entropy of Y given X as a scalar value.
    :rtype: float
    """
    return conditional_entropy(Y, X) / shanon_entropy(Y)
