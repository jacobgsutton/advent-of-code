ans = 0
s = open(0).read().strip()

prizes = s.split('\n\n')

BIG_NUM = 10000000000000

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
    
    end_x += BIG_NUM
    end_y += BIG_NUM

    # Why didn't I think of this from the start ugh :( all that recursion nonsense was completely unnecessary
    # 
    # alpha * a_dx + beta * b_dx = end_x
    # alpha * a_dy + beta * b_dy = end_y
    #
    # Solving for alpha and beta give: 
    
    alpha = (b_dy*end_x-b_dx*end_y)//(b_dy*a_dx-b_dx*a_dy)
    beta = (a_dy*end_x-a_dx*end_y)//(a_dy*b_dx-a_dx*b_dy)

    if ((b_dy*end_x-b_dx*end_y)%(b_dy*a_dx-b_dx*a_dy)==0 and 
        (a_dy*end_x-a_dx*end_y)%(a_dy*b_dx-a_dx*b_dy)==0): ans += 3*alpha + beta
    
print(ans)