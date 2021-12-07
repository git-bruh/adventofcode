import sys
from collections import defaultdict

positions = list(map(int, sys.stdin.read().split(",")))
min_fuel = -1

max_pos = max(positions)
extra = defaultdict(int)  # Remove this for part 1

for dest_pos in range(max_pos + 1):
    fuel = 0

    for position in positions:
        dist = abs(position - dest_pos)

        if dist not in extra:
            for i in range(dist):
                extra[dist] += i

        fuel += dist + extra[dist]

    if min_fuel == -1 or fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
