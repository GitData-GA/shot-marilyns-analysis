from .joint_entropy import joint_entropy
from .shanon_entropy import shanon_entropy


def conditional_entropy(Y, X):
    """
    Calculate the conditional entropy of Y given X.

    This function calculates the conditional entropy of Y given X. It calls the
    `joint_entropy` function to calculate the joint entropy of Y and X. It calls
    the `shanon_entropy` function to calculate the entropy of X. It subtracts the
    entropy of X from the joint entropy of Y and X to get the conditional entropy.

    :param Y: A NumPy array.
    :type Y: numpy.ndarray
    :param X: A NumPy array.
    :type X: numpy.ndarray
    :return: The conditional entropy of Y given X as a scalar value.
    :rtype: float
    """
    return joint_entropy(Y, X) - shanon_entropy(X)
