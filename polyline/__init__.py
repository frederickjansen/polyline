from .codec import PolylineCodec

__version__ = '1.3.2'


def decode(expression, precision=5):
    """
    Decode a polyline string into a set of coordinates.

    :param expression: Polyline string, e.g. 'u{~vFvyys@fS]'.
    :param precision: Precision of the encoded coordinates. Google Maps uses 5, OpenStreetMap uses 6.
        The default value is 5.
    :return: List of coordinate tuples
    """
    return PolylineCodec().decode(expression, precision)


def encode(coordinates, precision=5):
    """
    Encode a set of coordinates in a polyline string.

    :param coordinates: List of coordinate tuples, e.g. [(0, 0), (1, 0)].
    :param precision: Precision of the coordinates to encode. Google Maps uses 5, OpenStreetMap uses 6.
        The default value is 5.
    :return: The encoded polyline string.
    """
    return PolylineCodec().encode(coordinates, precision)


__all__ = ['decode', 'encode']
