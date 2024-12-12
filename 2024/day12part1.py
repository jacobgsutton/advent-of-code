ans = 0
m = open(0).read().splitlines()
r = len(m)
c = len(m[0])

visited = set()
def dfs(x, y, plant):
    if x < 0 or x >= c or y < 0 or y >= r or m[y][x] != plant:
        return (0,1)
    if (x, y) in visited: return (0, 0)

    visited.add((x, y))

    area = 1
    perm = 0
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        a, p = dfs(x+dx, y+dy, plant)
        area += a
        perm += p
    
    return (area, perm)

for i in range(r):
    for j in range(c):
        area, perm = dfs(j, i, m[i][j])
        # print(m[i][j], area, perm)
        ans += area * perm
print(ans)