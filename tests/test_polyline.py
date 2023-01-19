from random import uniform, randint
import time

import polyline


def test_decode_multiple_points():
    d = polyline.decode('gu`wFnfys@???nKgE??gE?????oK????fE??fE')
    assert d == [
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
    ]


def test_decode_multiple_points_precision():
    d = polyline.decode('_epolA~ieoOnF??~{Bo}@??o}@?????_|B????n}@??n}@', 6)
    assert d == [
        (40.64112, -8.654),
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
    ]


def test_decode_official_example():
    d = polyline.decode('_p~iF~ps|U_ulLnnqC_mqNvxq`@')
    assert d == [
        (38.500, -120.200),
        (40.700, -120.950),
        (43.252, -126.453)
    ]


def test_decode_geojson():
    d = polyline.decode('_p~iF~ps|U_ulLnnqC_mqNvxq`@', geojson=True)
    assert d == [
        (-120.200, 38.500),
        (-120.950, 40.700),
        (-126.453, 43.252)
    ]


def test_decode_official_example_precision():
    d = polyline.decode('_izlhA~rlgdF_{geC~ywl@_kwzCn`{nI', 6)
    assert d == [
        (38.500, -120.200),
        (40.700, -120.950),
        (43.252, -126.453)
    ]


def test_decode_single_point():
    d = polyline.decode('gu`wFf`ys@')
    assert d == [
        (40.641, -8.653)
    ]


def test_decode_single_point_precision():
    d = polyline.decode('o}oolAnkcoO', 6)
    assert d == [
        (40.641, -8.653)
    ]


def test_encode_multiple_points():
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
    assert e == 'gu`wFnfys@???nKgE??gE?????oK????fE??fE'


def test_encode_multiple_points_precision():
    e = polyline.encode([
        (40.64112345, -8.654),
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
    assert e == 'eepolA~ieoOtF??~{Bo}@??o}@?????_|B????n}@??n}@'

def test_encode_official_example():
    e = polyline.encode([
        (38.500, -120.200),
        (40.700, -120.950),
        (43.252, -126.453)
    ])
    assert e == '_p~iF~ps|U_ulLnnqC_mqNvxq`@'


def test_encode_geojson():
    e = polyline.encode([
        (-120.200, 38.500),
        (-120.950, 40.700),
        (-126.453, 43.252)
    ], geojson=True)
    assert e == '_p~iF~ps|U_ulLnnqC_mqNvxq`@'


def test_encode_official_example_precision():
    e = polyline.encode([
        (38.500, -120.200),
        (40.700, -120.950),
        (43.252, -126.453)
    ], 6)
    assert e == '_izlhA~rlgdF_{geC~ywl@_kwzCn`{nI'


def test_encode_single_point():
    e = polyline.encode([
        (40.64155, -8.65344)
    ])
    assert e == 'ux`wF~bys@'

    e = polyline.encode([
        (40.641552, -8.653441)
    ])
    assert e == 'ux`wF~bys@'


def test_encode_single_point_rounding():
    e = polyline.encode([
        (0, 0.000006),
        (0, 0.000002)
    ])
    assert e == '?A?@'


def test_rounding_py3_match_py2():
    e = polyline.encode([
        (36.05322, -112.084004),
        (36.053573, -112.083914),
        (36.053845, -112.083965)])
    assert e == 'ss`{E~kbkTeAQw@J'


def test_encode_single_point_precision():
    e = polyline.encode([
        (40.641123, -8.653321)
    ], 6)
    assert e == 'eepolAp_doO'

    e = polyline.encode([
        (40.6411233123, -8.6533214234)
    ], 6)
    assert e == 'eepolAp_doO'


def test_a_variety_of_precisions():
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
                    print(f"idx={idx}, dx={dx}, dy={dy}")
                else:
                    okays += 1

    assert okays == waypoints
    print(
        f"encoded and decoded {100 * okays / float(waypoints):.2f}% correctly for {waypoints} "
        f"waypoints @ {round(waypoints / patience, 0)} wp/sec")
