def rgb_to_hex(rgb):
    """
    Convert an RGB tuple to a hexadecimal color code.

    This function takes in an RGB tuple with three integer values (each ranging from 0 to 255).
    It formats the RGB values into a hexadecimal string using string formatting. Each RGB value
    is converted to a two-digit hexadecimal number.

    :param rgb: An RGB tuple with three integer values.
    :type rgb: tuple
    :return: A string representing the hexadecimal color code, starting with a '#' character.
    :rtype: str
    """
    return "#{:02x}{:02x}{:02x}".format(*rgb)
