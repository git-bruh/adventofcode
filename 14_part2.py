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

pairs = defaultdict(int)

for index in range(len(template) - 1):
    pairs[template[index] + template[index + 1]] += 1

# Not really my code, had to read another answer to solve the problem
# without modifying the string. Putting it in the repo just for my
# reference
for _ in range(40):
    new_pairs = defaultdict(int)

    for pair in pairs:
        ch = action_when_adjacent.get(pair)

        if not ch:
            continue

        start, end = pair

        # Make 2 new pairs
        new_pairs[start + ch] += pairs[pair]
        new_pairs[ch + end] += pairs[pair]

    pairs = new_pairs

element_count = defaultdict(int)

for key, value in pairs.items():
    for ch in key:
        element_count[ch] += value

# All letters are counted 2 times as they appear in 2 pairs, eg
# In "CCB", "C" occurs in "CC" and "CB" both.
# First and last never change as insertion is always in between 2 characters, so we double count them
element_count[template[0]] += 1
element_count[template[-1]] += 1

sort = sorted(element_count.values())
# Double counted
print((sort[-1] - sort[0]) / 2)
