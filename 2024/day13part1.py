import sys
from functools import cache

ans = 0
s = open(0).read().strip()

prizes = s.split('\n\n')

a_dx=0
a_dy=0
b_dx=0
b_dy=0
end_x=0
end_y=0

@cache
def min_cost(x_pos, y_pos):
    global a_dx, a_dy, b_dx, b_dy, end_x, end_y

    if x_pos > end_x or y_pos > end_y: return sys.maxsize
    elif x_pos == end_x and y_pos == end_y: return 0

    a_cost = min_cost(x_pos+a_dx, y_pos+a_dy)
    b_cost = min_cost(x_pos+b_dx, y_pos+b_dy)

    if a_cost < b_cost: return 3 + a_cost
    else: return 1 + b_cost

def nums(str_list):
    return [int(''.join(filter(lambda c: c.isnumeric(), str))) for str in str_list]

for prize in prizes:
    input = prize.splitlines()
    a = input[0].split(',')
    b = input[1].split(',')
    prize_pos = input[2].split(',')
    a_dx, a_dy = nums(a)
    b_dx, b_dy = nums(b)
    end_x, end_y = nums(prize_pos)

    val = min_cost(0, 0)
    if val < sys.maxsize: ans += val
    min_cost.cache_clear()

print(ans)