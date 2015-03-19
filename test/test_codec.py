import unittest

from polyline.codec import PolylineCodec


class PolylineCodecTestCase(unittest.TestCase):
    def setUp(self):
        self.codec = PolylineCodec()

    def test_decode_multiple_points(self):
        d = self.codec.decode('gu`wFnfys@???nKgE??gE?????oK????fE??fE')
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
        d = self.codec.decode('o}oolA~ieoO???~{Bo}@??o}@?????_|B????n}@??n}@', 6)
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
        d = self.codec.decode('_p~iF~ps|U_ulLnnqC_mqNvxq`@')
        self.assertEqual(d, [
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ])

    def test_decode_official_example_precision(self):
        d = self.codec.decode('_izlhA~rlgdF_{geC~ywl@_kwzCn`{nI', 6)
        self.assertEqual(d, [
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ])

    def test_decode_single_point(self):
        d = self.codec.decode('gu`wFf`ys@')
        self.assertEqual(d, [
            (40.641, -8.653)
        ])

    def test_decode_single_point_precision(self):
        d = self.codec.decode('o}oolAnkcoO', 6)
        self.assertEqual(d, [
            (40.641, -8.653)
        ])

    def test_encode_multiple_points(self):
        e = self.codec.encode([
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
        e = self.codec.encode([
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
        e = self.codec.encode([
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ])
        self.assertEqual(e, '_p~iF~ps|U_ulLnnqC_mqNvxq`@')

    def test_encode_official_example_precision(self):
        e = self.codec.encode([
            (38.500, -120.200),
            (40.700, -120.950),
            (43.252, -126.453)
        ], 6)
        self.assertEqual(e, '_izlhA~rlgdF_{geC~ywl@_kwzCn`{nI')

    def test_encode_single_point(self):
        e = self.codec.encode([
            (40.641, -8.653)
        ])
        self.assertEqual(e, 'gu`wFf`ys@')

    def test_encode_single_point_precision(self):
        e = self.codec.encode([
            (40.641, -8.653)
        ], 6)
        self.assertEqual(e, 'o}oolAnkcoO')
