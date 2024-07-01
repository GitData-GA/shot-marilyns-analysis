import numpy as np


def shanon_entropy(Y):
    """
    Shannon Entropy Calculation for a NumPy array.
    
    This function calculates the Shannon entropy of the input NumPy array `Y`. Shannon entropy 
    is a measure of uncertainty or information content in the array. It computes the entropy by 
    finding unique elements and their frequencies in `Y`, calculating the probability of each 
    unique element, and then applying the formula -sum(p * log2(p)), where p is the probability 
    of each element.
    
    :param Y: Input NumPy array for entropy calculation.
    :type Y: numpy.ndarray
    :return: Shannon entropy value of the input array `Y`.
    :rtype: float
    """
    unique, count = np.unique(Y, return_counts=True, axis=0)
    prob = count / len(Y)
    entropy = np.sum((-1) * prob * np.log2(prob))
    return entropy
