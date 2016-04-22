import itertools
import six


class PolylineCodec(object):
    def _pcitr(self, iterable):
        return six.moves.zip(iterable, itertools.islice(iterable, 1, None))

    def _write(self, output, curr_value, prev_value, factor):
        curr_value = int(round(curr_value * factor, 0))
        prev_value = int(round(prev_value * factor, 0))
        coord = curr_value - prev_value
        coord <<= 1
        coord = coord if coord >= 0 else ~coord

        while coord >= 0x20:
            output.write(six.unichr((0x20 | (coord & 0x1f)) + 63))
            coord >>= 5

        output.write(six.unichr(coord + 63))

    def _trans(self, value, index):
        byte, result, shift = None, 0, 0

        while (byte is None or byte >= 0x20):
            byte = ord(value[index]) - 63
            index += 1
            result |= (byte & 0x1f) << shift
            shift += 5
            comp = result & 1

        return ~(result >> 1) if comp else (result >> 1), index

    def decode(self, expression, precision=5):
        coordinates, index, lat, lng, length, factor = [], 0, 0, 0, len(expression), float(10 ** precision)

        while (index < length):
            lat_change, index = self._trans(expression, index)
            lng_change, index = self._trans(expression, index)
            lat += lat_change
            lng += lng_change
            coordinates.append((lat / factor, lng / factor))

        return coordinates

    def encode(self, coordinates, precision=5):
        output, factor = six.StringIO(), int(10 ** precision)

        self._write(output, coordinates[0][0], 0, factor)
        self._write(output, coordinates[0][1], 0, factor)

        for prev, curr in self._pcitr(coordinates):
            self._write(output, curr[0], prev[0], factor)
            self._write(output, curr[1], prev[1], factor)

        return output.getvalue()
