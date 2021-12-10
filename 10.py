import sys

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

closing = {"(": ")", "[": "]", "{": "}", "<": ">"}

illegal_sum = 0

for line in sys.stdin.read().split("\n"):
    stack = []

    for c in line:
        if closing.get(c):  # Start sequence
            stack.append(c)
        elif c != closing.get(
            stack.pop()
        ):  # End sequence, but doesn't match the last start sequence
            illegal_sum += points[c]
            break

print(illegal_sum)
