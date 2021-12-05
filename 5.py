import sys
from collections import defaultdict

# Whether to check 45 degree diagonals
PART2 = False


def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    if x < 0:
        return -1


co_ords = defaultdict(int)

for line in sys.stdin.read().split("\n"):
    if not line:
        continue

    line = line.split(" -> ")

    x1, y1, x2, y2 = map(int, line[0].split(",") + line[1].split(","))
    sign_x, sign_y = map(sign, (x2 - x1, y2 - y1))

    # Max difference, ignoring sign
    size = 1 + max(abs(x1 - x2), abs(y1 - y2))

    if PART2 or sign_x == 0 or sign_y == 0:
        for i in range(size):
            co_ords[(x1 + i * sign_x, y1 + i * sign_y)] += 1

print(sum(i >= 2 for i in co_ords.values()))
