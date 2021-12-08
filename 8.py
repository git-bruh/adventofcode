import sys

segmap = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

counter = 0

for line in sys.stdin.read().split("\n"):
    if not line:
        continue

    signals, output = line.split(" | ")

    for value in output.split():
        if segmap.get(len(value)):
            counter += 1

print(counter)
