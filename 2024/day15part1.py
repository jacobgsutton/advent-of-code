ans = 0
m, cmds = open(0).read().split('\n\n')
m = list(map(list, m.splitlines()))
r = len(m)
c = len(m[0])

def move(x, y, dx, dy, item):
    if m[y+dy][x+dx] == '#': return False
    if m[y+dy][x+dx] == 'O': 
        if move(x+dx, y+dy, dx, dy, 'O'):
            m[y][x] = '.'
            m[y+dy][x+dx] = item
            return True
        else: return False
    m[y][x] = '.'
    m[y+dy][x+dx] = item
    return True

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
    # if not int(input(f"Continue with cmd {cmd}? (0/1): ")): break

    if cmd == '<': dx, dy = -1, 0
    elif cmd == '>': dx, dy = 1, 0
    elif cmd == 'v': dx, dy = 0, 1
    else: dx, dy = 0, -1
    if move(pos[0], pos[1], dx, dy, '@'):
        pos[0]+=dx
        pos[1]+=dy

for i in range(r):
    for j in range(c):
        if m[i][j] == 'O':
            ans += 100 * i + j
print(ans)