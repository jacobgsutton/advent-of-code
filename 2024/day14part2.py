import re

lines = open(0).read().splitlines()

R=103
C=101 

robots = []

def print_robots():
    m = [[0 for _ in range(C)] for _ in range(R)]
    for robot in robots:
        m[robot[0]][robot[1]]+=1
    for i in range(R):
        for j in range(C):
            if m[i][j] == 0: print('.', end='')
            else: print(m[i][j], end='')
        print()
    print()

def has_lg_connected_row(size):
    m = [[0 for _ in range(C)] for _ in range(R)]
    for robot in robots:
        m[robot[0]][robot[1]]+=1
    for i in range(R):
        streak = 0
        for j in range(C):
            if m[i][j] > 0: streak += 1
            else: streak = 0
            if streak >= size: return True
    return False

for line in lines:
    px,py,vx,vy = map(int, re.findall(r'-?\d+', line))
    robots.append([py, px, vy, vx])

ans = 0
while ans < 15000:
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % R
        robot[1] = (robot[1] + robot[3]) % C
    ans += 1
    if has_lg_connected_row(10):
        break
        # print(ans)
        # print_robots()

print(ans)    
print_robots()

# This is how I found it at first which required watching my terminal output 
# for the tree to appear after a few minutes. The instructions were so vague.
#
# ans = 0
# while True:
#     for robot in robots:
#         robot[0] = (robot[0] + robot[2]) % R
#         robot[1] = (robot[1] + robot[3]) % C
#     ans += 1
#     print(ans)
#     print_robots()
