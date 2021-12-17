import sys
import math

buf = sys.stdin.read()
buf = buf[buf.index("x") :]

x, y = [
    map(int, line.split(".."))
    for line in buf.replace("x=", "").replace("y=", "").split(", ")
]

x1, x2, y1, y2 = *x, *y


def velocity_check(vel_x, vel_y, x1, x2, y1, y2):
    curr_x = 0
    curr_y = 0

    max_y = -math.inf

    while True:
        if curr_y > max_y:
            max_y = curr_y

        if curr_x >= x1 and curr_x <= x2 and curr_y >= y1 and curr_y <= y2:
            return (max_y, True)

        if curr_x > x2 or curr_y < y1:
            return (max_y, False)

        curr_x += vel_x
        curr_y += vel_y

        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1

        vel_y -= 1


max_y = -math.inf
counter = 0

PART2 = True

iterator = range(y1 * 2, -(y1 * 2)) if PART2 else range(-(y1 * 2))

for y in iterator:
    for x in range(x2 + 1):
        my, success = velocity_check(x, y, x1, x2, y1, y2)

        if success:
            counter += 1

            if my > max_y:
                max_y = my

print(counter, max_y)
