import sys

buf = []

for line in sys.stdin.read().split("\n"):
    if not line:
        continue

    buf.append(list(map(int, line)))


def append_if_get(adjacent, buf, row, index):
    # -1 means last element, but here it means that the item doesn't exist
    if index == -1 or row == -1:
        return False

    try:
        adjacent.append(buf[row][index])
        return True
    except IndexError:
        return False


visited = {}


def get_basin(index, row, buf):
    basin = []

    for row_get, index_get in [
        [row, index - 1],
        [row, index + 1],
        [row - 1, index],
        [row + 1, index],
    ]:
        if (row_get, index_get) in visited:
            continue

        visited[(row_get, index_get)] = True

        if append_if_get(basin, buf, row_get, index_get):
            if basin[-1] == 9:
                basin.pop()
            else:
                basin.extend(get_basin(index_get, row_get, buf))

    return basin


lens = []

for row_index, line in enumerate(buf):
    for num_index, num in enumerate(line):
        lens.append(len(get_basin(num_index, row_index, buf)))

product = 1

for length in sorted(lens)[-3:]:
    product *= length

print(product)
