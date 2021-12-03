import sys

COLUMNS = 12


def count_bits(lines, start):
    count = {"0": 0, "1": 0}
    nums_starting_with = {"0": [], "1": []}

    for line in lines:
        if line == "":
            continue

        count[line[start]] += 1
        nums_starting_with[line[start]].append(line)

    return (count, nums_starting_with)


def get_rating(column, count, nums_starting_with, value_fn):
    c_max = value_fn(count)

    if len(nums_starting_with[c_max]) == 1:
        return nums_starting_with[c_max][0]

    if column != 0:
        count, nums_starting_with = count_bits(
            nums_starting_with[c_max], column
        )

    nums = nums_starting_with[c_max]

    return get_rating(column + 1, count, nums_starting_with, value_fn)


def val_oxygen(d):
    if d["0"] == d["1"]:
        return "1"

    return max(d, key=d.get)


def val_co2(d):
    if d["0"] == d["1"]:
        return "0"

    return min(d, key=d.get)


count, nums_starting_with = count_bits(sys.stdin.read().split("\n"), 0)

oxygen = get_rating(0, count, nums_starting_with, val_oxygen)
co2 = get_rating(0, count, nums_starting_with, val_co2)

print(oxygen, co2, int(oxygen, 2) * int(co2, 2))
