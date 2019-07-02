Introduction
============

``polyline`` is a Python implementation of Google's Encoded Polyline Algorithm
Format (http://goo.gl/PvXf8Y). It is essentially a port of
https://github.com/mapbox/polyline built with Python 2 and 3 support in mind.

Installation
============

``polyline`` can be installed using ``pip`` or ``easy_install``::

    $ pip install polyline
    or
    $ easy_install polyline

API Documentation
=================

Encoding
--------

To get the encoded polyline representation of a given set of (lat, lon) coordinates::

    import polyline
    polyline.encode([(38.5, -120.2), (40.7, -120.9), (43.2, -126.4)], 5)

This should return ``_p~iF~ps|U_ulL~ugC_hgN~eq`@``.

You can set the required precision with the optional ``precision`` parameter. The default value is 5.

You can encode (lon, lat) tuples by setting ``geojson=True``.

Decoding
--------

To get a set of coordinates represented by a given encoded polyline string::

    import polyline
    polyline.decode('u{~vFvyys@fS]')

This should return ``[(40.63179, -8.65708), (40.62855, -8.65693)]`` in (lat, lon) order.

You can decode into (lon, lat) tuples by setting ``geojson=True``.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
