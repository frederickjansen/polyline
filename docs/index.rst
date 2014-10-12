.. polyline documentation master file, created by
   sphinx-quickstart on Sat Oct 11 16:14:05 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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

To get the encoded polyline representation of a given set of coordinates::

    from polyline.codec import PolylineCodec
    PolylineCodec().encode([(38.5, -120.2), (40.7, -120.9), (43.2, -126.4)])

This should return ``_p~iF~ps|U_ulL~ugC_hgN~eq`@``.

Decoding
--------

To get the set of coordinates reprented by a given encoded polyline string::

    from polyline.codec import PolylineCodec
    PolylineCodec().decode('u{~vFvyys@fS]')

This should return ``[(40.63179, -8.65708), (40.62855, -8.65693)]``.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
