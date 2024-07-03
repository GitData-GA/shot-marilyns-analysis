def convert_to_numerical_tuple(tup):
    """
    Convert Tuple Elements to Floats.

    This function takes a tuple of elements and converts each element to a float. It
    returns a new tuple containing the converted float values.

    :param tup: Input tuple containing elements to be converted.
    :type tup: tuple
    :return: A tuple with all elements converted to floats.
    :rtype: tuple
    """
    numerical_tuple = tuple(float(item) for item in tup)
    return numerical_tuple
