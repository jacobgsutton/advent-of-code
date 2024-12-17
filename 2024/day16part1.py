from heapq import heappush, heappop
from math import sqrt
import sys

m=open(0).read().splitlines()
r = len(m)
c = len(m[0])

ROTATION_COST = 1000
INF = sys.maxsize

class Node:
    def __init__(self, pos, facing):
        self.pos = pos
        self.facing = facing

    def __hash__(self):
        return hash(self.pos)
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.pos == other.pos
        return False

    def __lt__(self, other):
        return Node.f_score[self] < Node.f_score[other]

def L2(n1, n2):
    return sqrt((n2.pos[0]-n1.pos[0])**2+(n2.pos[1]-n1.pos[1])**2)

def rot_cost(n1, n2):
    dist_y = n2.pos[0] - n1.pos[0]
    dist_x = n2.pos[1] - n1.pos[1]
    dir_y = dist_y/abs(dist_y) if dist_y != 0 else 0
    dir_x = dist_x/abs(dist_x) if dist_x != 0 else 0 

    if n1.facing[0] == dir_y and n1.facing[1] == dir_x: return 0
    elif dir_y != 0 and dir_x != 0:
        val = 0
        if n1.facing[0] != dir_y: val += ROTATION_COST
        if n1.facing[1] != dir_x: val += ROTATION_COST
        return val
    elif (-n1.facing[1], n1.facing[0]) == (dir_y, dir_x) or  (n1.facing[1], -n1.facing[0]) == (dir_y, dir_x): return ROTATION_COST
    return 2*ROTATION_COST

def h(n):
    return L2(n, e_pos) + rot_cost(n, e_pos)

def neighbor_dist(n1, n2):
    return 1 + rot_cost(n1, n2)

def get_path(came_from, cn):
    path = [cn]
    while cn in came_from.keys():
        cn = came_from[cn]
        path.append(cn)
    return path

def astar():
    open_set = [s_pos]

    came_from = {}

    g_score = {s_pos: 0}
    Node.f_score = {s_pos: h(s_pos)}

    while len(open_set) != 0:
        cn = heappop(open_set)
        if cn.pos == e_pos.pos: return (get_path(came_from, cn), g_score[e_pos])

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if m[cn.pos[0]+dy][cn.pos[1]+dx] == '#': continue
            neighbor = Node((cn.pos[0]+dy, cn.pos[1]+dx), (dy, dx))

            tentative_g_score = g_score[cn] + neighbor_dist(cn, neighbor)

            if tentative_g_score < g_score.get(neighbor, INF):

                came_from[neighbor] = cn

                g_score[neighbor] = tentative_g_score
                Node.f_score[neighbor] = tentative_g_score + h(neighbor)
                if neighbor not in open_set: heappush(open_set, neighbor)

    return (-1, -1) #Couldn't find end (shouldn't happen)

for i in range(r):
    for j in range(c):
        if m[i][j] == 'S':
            s_pos = Node((i, j), (0, 1))
        elif m[i][j] == 'E':
            e_pos = Node((i, j), (0,0))

r_path, cost = astar()
r_path = [node.pos for node in r_path]

print(cost)
# print('\n'.join([''.join('O' if (i, j) in r_path else m[i][j] for j in range(c)) for i in range(r)]))

