import sys

points = {")": 1, "]": 2, "}": 3, ">": 4}

closing = {"(": ")", "[": "]", "{": "}", "<": ">"}

total_points = []

for line in sys.stdin.read().split("\n"):
    stack = []
    broken = False

    for c in line:
        if closing.get(c):  # Start sequence
            stack.append(c)
        elif c != closing.get(
            stack.pop()
        ):  # End sequence, but doesn't match the last start sequence
            broken = True
            break

    if not broken and len(stack) > 0:
        line_points = 0

        for c in stack[::-1]:
            line_points = (line_points * 5) + points[closing[c]]

        total_points.append(line_points)

print(sorted(total_points)[int(len(total_points) / 2)])
