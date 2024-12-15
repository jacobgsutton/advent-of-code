from copy import deepcopy
ans = 0
old_m, cmds = open(0).read().split('\n\n')
old_m = list(map(list, old_m.splitlines()))
r = len(old_m)
c = len(old_m[0])
m = []

def move(x, y, dx, dy, item, no_l_br, no_r_br):
    global m
    backup_m = deepcopy(m)
    if m[y+dy][x+dx] == '#': return False
    elif m[y+dy][x+dx] == '[':
        if dy == 0 or no_r_br:
            if move(x+dx, y+dy, dx, dy, '[', False, False):
                m[y][x] = '.'
                m[y+dy][x+dx] = item
                return True
            else: return False
        else:
            if move(x+dx, y+dy, dx, dy, '[', False, True) and move(x+dx+1, y+dy, dx, dy, ']', True, False):
                m[y][x] = '.'
                m[y+dy][x+dx] = item
                return True
            else:
                m = deepcopy(backup_m)
                return False
    elif m[y+dy][x+dx] == ']':
        if dy == 0 or no_l_br:
            if move(x+dx, y+dy, dx, dy, ']', False, False):
                m[y][x] = '.'
                m[y+dy][x+dx] = item
                return True
            else: return False
        else:
            if move(x+dx, y+dy, dx, dy, ']', True, False) and move(x+dx-1, y+dy, dx, dy, '[', False, True):
                m[y][x] = '.'
                m[y+dy][x+dx] = item
                return True
            else:
                m = deepcopy(backup_m)
                return False
    m[y][x] = '.'
    m[y+dy][x+dx] = item
    return True

for i in range(r):
    row = []
    for j in range(c):
        if old_m[i][j] == '#': row += ['#', '#']
        elif old_m[i][j] == 'O': row += ['[', ']']
        elif old_m[i][j] == '.': row += ['.', '.']
        else: row += ['@', '.']
    m.append(row)
r = len(m)
c = len(m[0])

for i in range(r):
    for j in range(c):
        if m[i][j] == '@':
            pos = [j, i]
            break
    else: continue
    break

for cmd in ''.join(cmds.split()):
    
    # print('\n'.join([''.join(line) for line in m]))
    # print()
    # print(cmd)
    # if not int(input(f"Continue with cmd {cmd}? (0/1): ")): break

    if cmd == '<': dx, dy = -1, 0
    elif cmd == '>': dx, dy = 1, 0
    elif cmd == 'v': dx, dy = 0, 1
    else: dx, dy = 0, -1
    if move(pos[0], pos[1], dx, dy, '@', False, False):
        pos[0]+=dx
        pos[1]+=dy

for i in range(r):
    for j in range(c):
        if m[i][j] == '[':
            ans += 100 * i + j
print(ans)