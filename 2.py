from dataclasses import dataclass
import enum
import sys

class OTYPE(enum.Enum):
	FORWARD = 0
	DOWN = 1
	UP = 2

@dataclass
class OP:
	op: OTYPE
	value: int

str_to_op = {
	"forward": OTYPE.FORWARD,
	"down": OTYPE.DOWN,
	"up": OTYPE.UP,
}

def get_op(line):
	line = line.split()
	return OP(str_to_op[line[0]], int(line[1]))

ops = [get_op(line) for line in sys.stdin.read().split("\n") if line != ""]

horizontal = 0
depth = 0

for op in ops:
	print(op)

	match op.op:
		case OTYPE.FORWARD:
			horizontal += op.value
		case OTYPE.DOWN:
			depth += op.value
		case OTYPE.UP:
			depth -= op.value

print(f"Horizontal: {horizontal}, Depth: {depth}, Result: {horizontal * depth}")
