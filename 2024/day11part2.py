stones = tuple(map(int, open(0).read().split(' ')))
n = 75

cache = {}

def dnc(stones, depth):
    global n
    # print(depth, stones)
    if len(stones) == 0: return 0
    if (stones, depth) in cache: return cache[(stones, depth)]
    if depth == n: return len(stones)

    new_stones = []
    for s in stones:
        if s == 0: new_stones.append(1)
        elif len(str(s)) % 2 == 0:
            new_stones.append(int(str(s)[:len(str(s))//2]))
            new_stones.append(int(str(s)[len(str(s))//2:]))
        else: new_stones.append(s*2024)

    val = dnc(tuple(new_stones[:len(new_stones)//2]), depth+1) + dnc(tuple(new_stones[len(new_stones)//2:]), depth+1)
    cache[(stones, depth)] = val
    return val

print(dnc(stones, 0))