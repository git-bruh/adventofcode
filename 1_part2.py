import sys

nums = [int(line) for line in sys.stdin.read().split("\n") if line != ""]

psums = -1
larger = 0

for i in range(2, len(nums)):
    sums = nums[i] + nums[i - 1] + nums[i - 2]

    if psums != -1 and sums > psums:
        larger += 1

    psums = sums

print(f"Larger: {larger}")
