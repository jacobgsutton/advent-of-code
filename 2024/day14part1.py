import re

lines = open(0).read().splitlines()

R=103
C=101 
N=100

quads = [(range(0, R//2), range(C//2+1, C)), (range(0, R//2), range(0, C//2)), (range(R//2+1, R), range(0, C//2)), (range(R//2+1, R), range(C//2+1, C))]
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

for line in lines:
    px,py,vx,vy = map(int, re.findall(r'-?\d+', line))
    robots.append([py, px, vy, vx])

for _ in range(N):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % R
        robot[1] = (robot[1] + robot[3]) % C

quad_cnts = [0,0,0,0]
for robot in robots:
    for i, quad in enumerate(quads):
        if robot[0] in quad[0] and robot[1] in quad[1]:
            quad_cnts[i] += 1
            break

# print_robots()

ans = 1
for quad_cnt in quad_cnts:
    ans *= quad_cnt
print(ans)