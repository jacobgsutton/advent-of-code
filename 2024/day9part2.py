ans = 0
m = open(0).read().strip()
d = []
n = 0
files = []
empty_space = []

for i, c in enumerate(m):
    if i % 2 == 0:
        files.append([len(d), int(c)])
        d.extend(str(n) for _ in range(int(c)))
        n+=1
    elif int(c) != 0:
        empty_space.append([len(d), int(c)])
        d.extend('.' for _ in range(int(c)))

for f in files[::-1]:
    #print(''.join(d))
    for e in empty_space:
        if e[0] > f[0]: break
        if f[1] <= e[1]:
            for i in range(f[1]):
                d[e[0]+i]=d[f[0]+f[1]-i-1]
                d[f[0]+f[1]-i-1]='.'
            e[1] = e[1]-f[1]
            e[0] = e[0]+f[1]
            break
#print(''.join(d))
for i, id in enumerate(d):
    if id == '.': continue
    ans += i * int(id)
print(ans)