ans = 0
m = open(0).read().splitlines()
r = len(m)
c = len(m[0])
visited = set()

def dfs(x, y, last):
    if x < 0 or x >= c or y < 0 or y >= r or (x, y) in visited:
        return 0

    node = int(m[y][x])

    if last != node-1:
        return 0
    
    visited.add((x, y))

    if node == 9:
        return 1

    paths = 0
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        paths += dfs(x+dx, y+dy, node)
    return paths

for i in range(r):
    for j in range(c):
        if m[i][j] == '0':
            ans += dfs(j, i, -1)
            visited.clear()

print(ans)