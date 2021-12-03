import sys

columns = 12
count = [{"0": 0, "1": 0} for _ in range(columns)]

for line in sys.stdin.read().split("\n"):
    for column, bit in enumerate(line):
        count[column][bit] += 1

binary_gamma = ""
binary_epsilon = ""

flip = {"0": "1", "1": "0"}

for c in count:
    # Key with max value
    c_max = max(c, key=c.get)

    binary_gamma += c_max
    binary_epsilon += flip[c_max]

binary_gamma = int(binary_gamma, 2)
binary_epsilon = int(binary_epsilon, 2)

print(
    f"Gamma: {binary_gamma}, Epsilon: {binary_epsilon}, "
    f"Power: {binary_gamma * binary_epsilon}"
)
