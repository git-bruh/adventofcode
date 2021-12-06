import sys

MAX_TIMER = 8
SIMULATE_DAYS = 256  # 18 for part 1
RESET_TIMER = 6

days = [0 for i in range(MAX_TIMER + 1)]

for timer in map(int, sys.stdin.read().split(",")):
    days[timer] += 1

for _ in range(SIMULATE_DAYS):
    new = days[0]

    for timer, num_fish in enumerate(days):
        if timer == 0:
            days[timer] = 0
        else:
            days[timer] = 0
            days[timer - 1] += num_fish

    # Add new fish at the end so that we satisfy the condition:
    # "The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day."
    days[RESET_TIMER] += new
    days[MAX_TIMER] += new

print(sum(days))
