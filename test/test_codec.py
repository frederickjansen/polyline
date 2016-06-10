import unittest
from random import uniform, randint
import time

import polyline


class PolylineCodecTestCase(unittest.TestCase):

    def test_decode_multiple_points(self):
        d = polyline.decode('gu`wFnfys@???nKgE??gE?????oK????fE??fE')
        self.assertEqual(d, [
            (40.641, -8.654),
            (40.641, -8.654),
            (40.641, -8.656),
            (40.642, -8.656),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.641, -8.653),
            (40.641, -8.654)
        ])

    def test_decode_multiple_points_precision(self):
        d = polyline.decode('o}oolA~ieoO???~{Bo}@??o}@?????_|B????n}@??n}@', 6)
        self.assertEqual(d, [
            (40.641, -8.654),
            (40.641, -8.654),
            (40.641, -8.656),
            (40.642, -8.656),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.641, -8.653),
            (40.641, -8.654)
        ])

    def test_decode_official_example(self):
        d = polyline.decode('_p~iF~ps|U_ulLnnqC_mqNvxq`@')
        self.assertEqual(d, [
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ])

    def test_decode_official_example_precision(self):
        d = polyline.decode('_izlhA~rlgdF_{geC~ywl@_kwzCn`{nI', 6)
        self.assertEqual(d, [
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ])

    def test_decode_single_point(self):
        d = polyline.decode('gu`wFf`ys@')
        self.assertEqual(d, [
            (40.641, -8.653)
        ])

    def test_decode_single_point_precision(self):
        d = polyline.decode('o}oolAnkcoO', 6)
        self.assertEqual(d, [
            (40.641, -8.653)
        ])

    def test_encode_multiple_points(self):
        e = polyline.encode([
            (40.641, -8.654),
            (40.641, -8.654),
            (40.641, -8.656),
            (40.642, -8.656),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.641, -8.653),
            (40.641, -8.654)
        ])
        self.assertEqual(e, 'gu`wFnfys@???nKgE??gE?????oK????fE??fE')

    def test_encode_multiple_points_precision(self):
        e = polyline.encode([
            (40.641, -8.654),
            (40.641, -8.654),
            (40.641, -8.656),
            (40.642, -8.656),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.655),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.642, -8.653),
            (40.641, -8.653),
            (40.641, -8.654)
        ], 6)
        self.assertEqual(e, 'o}oolA~ieoO???~{Bo}@??o}@?????_|B????n}@??n}@')

    def test_encode_official_example(self):
        e = polyline.encode([
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ])
        self.assertEqual(e, '_p~iF~ps|U_ulLnnqC_mqNvxq`@')

    def test_encode_official_example_precision(self):
        e = polyline.encode([
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ], 6)
        self.assertEqual(e, '_izlhA~rlgdF_{geC~ywl@_kwzCn`{nI')

    def test_encode_single_point(self):
        e = polyline.encode([
            (40.641, -8.653)
        ])
        self.assertEqual(e, 'gu`wFf`ys@')

    def test_encode_single_point_rounding(self):
        e = polyline.encode([
            (0, 0.000006),
            (0, 0.000002)
        ])
        self.assertEqual(e, '?A?@')

    def test_rounding_py3_match_py2(self):
        e = polyline.encode([
            (36.05322, -112.084004),
            (36.053573, -112.083914),
            (36.053845, -112.083965)])
        self.assertEqual(e, 'ss`{E~kbkTeAQw@J')

    def test_encode_single_point_precision(self):
        e = polyline.encode([
            (40.641, -8.653)
        ], 6)
        self.assertEqual(e, 'o}oolAnkcoO')

    def test_a_variety_of_precisions(self):
        """uses a generator to create a variety of lat-lon's across the global
            and tests a range of precision settings from 4 to 8"""

        def generator():
            while True:
                coords = []
                for i in range(2, randint(4, 10)):
                    lat, lon = uniform(-180.0, 180.0), uniform(-180.0, 180.0)
                    coords.append((lat, lon))
                yield coords

        patience = 3  # seconds.
        waypoints, okays = 0, 0

        g = generator()
        start = time.time()
        while time.time() < start + patience:
            precision = randint(4, 8)
            wp = next(g)
            waypoints += len(wp)
            poly = polyline.encode(wp, precision)
            wp2 = polyline.decode(poly, precision)
            if wp == wp2:
                okays += len(wp2)
            else:
                for idx, _ in enumerate(wp):
                    dx, dy = abs(wp[idx][0] - wp2[idx][0]), abs(wp[idx][1] - wp2[idx][1])
                    if dx > 10 ** -(precision - 1) or dy > 10 ** -(precision - 1):
                        print("idx={}, dx={}, dy={}".format(idx, dx, dy))
                    else:
                        okays += 1

        assert okays == waypoints
        print("encoded and decoded {0:.2f}% correctly for {1} waypoints @ {2} wp/sec".format(
            100 * okays / float(waypoints),
            waypoints,
            round(waypoints / patience, 0)))
