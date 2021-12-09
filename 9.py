import sys

buf = []

for line in sys.stdin.read().split("\n"):
    if not line:
        continue

    buf.append(list(map(int, line)))


def append_if_get(adjacent, buf, row, index):
    # -1 means last element, but here it means that the item doesn't exist
    if index == -1 or row == -1:
        return

    try:
        adjacent.append(buf[row][index])
    except IndexError:
        pass


def get_adjacent(index, row, buf):
    adjacent = []

    for row_get, index_get in [
        [row, index - 1],
        [row, index + 1],
        [row - 1, index],
        [row + 1, index],
    ]:
        append_if_get(adjacent, buf, row_get, index_get)

    return adjacent


total_sum = 0

for row_index, line in enumerate(buf):
    for num_index, num in enumerate(line):
        adjacent = get_adjacent(num_index, row_index, buf)

        try:
            if num < min(adjacent):
                total_sum += num + 1
        except ValueError:
            pass

print(total_sum)
