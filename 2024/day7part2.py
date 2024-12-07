cache = {}
#still really slow with caching, but works after a few minutes 
#the better way to do it that i've seen is to use recursion by treating rhs[:-1] as a sub problem. I was close to seeing this, but overcomplicated things by committing to the brute force method + cache
def calc(rhs, i, x, y):
    if i == 0:
        return rhs[i]
    val = cache.get((i,x,y))
    if val != None:
        return val
    val = calc(rhs, i-1, x>>1, y>>1)
    if x & 1:
        if y & 1:
            cache[(i,x,y)]=int(str(val)+str(rhs[i]))
            return int(str(val)+str(rhs[i]))
        else:
            cache[(i,x,y)]=val * rhs[i]
            return val * rhs[i]
    else:
        if y & 1:
            cache[(i,x,y)]=int(str(val)+str(rhs[i]))
            return int(str(val)+str(rhs[i]))
        else:
            cache[(i,x,y)]=val + rhs[i]
            return val + rhs[i]

ans = 0

eqs_in = open(0)
eqs = list()

for eq in eqs_in:
    lhs, rhs = eq.split(': ')
    eqs.append((int(lhs), list(map(int, rhs.split(' ')))))

for eq in eqs:
    b = 2**(len(eq[1])-1)
    for x in range(b):
        for y in range(b):
            rhs = calc(eq[1], len(eq[1])-1, x, y)
            if rhs == eq[0]:
                ans += rhs
                break
        else:
            continue
        break
    cache.clear()
print(ans)