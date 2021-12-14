import sys
from collections import defaultdict

buf = sys.stdin.read().split("\n")

template = list(buf[0])
action_when_adjacent = {}

for line in buf[2:]:
    if not line:
        continue

    adjacent, action = line.split(" -> ")
    action_when_adjacent[adjacent] = action

for _ in range(10):
    template_copy = template.copy()

    for index in range(len(template) - 1):
        action = action_when_adjacent.get(
            template[index] + template[index + 1]
        )

        if action:
            inserted = len(template_copy) - len(template)
            template_copy.insert(index + inserted + 1, action)

    if len(template_copy) - len(template) == 0:
        break

    template = template_copy

occurance = defaultdict(int)

for ch in template:
    occurance[ch] += 1

sort = sorted(occurance.values())

print(*template, sep="")
print(sort[-1] - sort[0])
