import sys
from collections import OrderedDict


buf = sys.stdin.read()

boards = []

max_nums = 5
nums_per_board = max_nums * max_nums
current_board = 0

for index, num in enumerate(buf[buf.index("\n") :].split()):
    if index != 0 and index % nums_per_board == 0:
        current_board += 1

    if len(boards) < (current_board + 1):
        boards.append(OrderedDict())

    boards[current_board][int(num)] = False  # Not marked

draws = [int(i) for i in buf[: buf.index("\n")].split(",")]


def marked(board):
    sum_unmarked = 0

    cols = [True for i in range(max_nums)]
    rows = [True for i in range(max_nums)]

    items = list(board.items())

    for index in range(0, nums_per_board, max_nums):
        row_index = int(index / max_nums)

        for inner_index, item in enumerate(items[index : max_nums + index]):
            cols[inner_index] = cols[inner_index] and item[1]
            rows[row_index] = rows[row_index] and item[1]

            if not item[1]:
                sum_unmarked += item[0]

    return (any(cols) or any(rows), sum_unmarked)


for draw in draws:
    won = False

    for board in boards:
        if draw not in board:
            continue

        board[draw] = True
        is_marked, sum_unmarked = marked(board)

        if is_marked:
            print(sum_unmarked * draw)

            won = True
            break

    if won:
        break
