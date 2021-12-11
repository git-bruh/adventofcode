import sys
import itertools

matrix = []

for line in sys.stdin.read().split("\n"):
    if line:
        matrix.append(list(map(int, line)))


def flash_adjacent(row, col, buf, flashed):
    if buf[row][col] <= 9 or (row, col) in flashed:
        return

    # An octopus can only flash at most once per step
    flashed[(row, col)] = True

    for row_get, col_get in [
        [row, col - 1],
        [row, col + 1],
        [row - 1, col],
        [row + 1, col],
        # Diagonals
        [row - 1, col - 1],
        [row - 1, col + 1],
        [row + 1, col - 1],
        [row + 1, col + 1],
    ]:
        if row_get < 0 or col_get < 0:
            continue

        try:
            buf[row_get][col_get] += 1
            flash_adjacent(row_get, col_get, buf, flashed)
        except IndexError:
            pass


PART2 = True

result = 0
iterator = itertools.count(1) if PART2 else range(100)

for step in iterator:
    flashed = {}

    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            matrix[row_index][col_index] += 1

    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            flash_adjacent(row_index, col_index, matrix, flashed)

    # Must reset after flashing
    for flash in flashed:
        row, col = flash
        matrix[row][col] = 0

    if PART2 and len(flashed) == len(matrix) * len(matrix[0]):
        result = step
        break

    if not PART2:
        result += len(flashed)

for line in matrix:
    print(*line, sep="")

print(result)
