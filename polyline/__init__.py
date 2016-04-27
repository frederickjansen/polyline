__version__ = '1.2.1'

from .codec import PolylineCodec
def decode(expression, precision=5):
    return PolylineCodec().decode(expression, precision)
    
def encode(coordinates, precision=5):
    return PolylineCodec().encode(coordinates, precision)

__all__ = ['decode', 'encode']
