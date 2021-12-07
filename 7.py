import sys
from collections import defaultdict

positions = list(map(int, sys.stdin.read().split(",")))
min_fuel = -1

max_pos = max(positions)

for dest_pos in range(max_pos + 1):
    fuel = 0

    for position in positions:
        dist = abs(position - dest_pos)
        dist += int((dist * (dist - 1) / 2))  # Sum, remove for part 1

        fuel += dist

    if min_fuel == -1 or fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
