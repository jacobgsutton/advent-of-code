stones = list(map(int, open(0).read().split(' ')))
n = 25

for i in range(n):
    # print(stones)
    new_stones = []
    for s in stones:
        if s == 0: new_stones.append(1)
        elif len(str(s)) % 2 == 0:
            new_stones.append(int(str(s)[:len(str(s))//2]))
            new_stones.append(int(str(s)[len(str(s))//2:]))
        else: new_stones.append(s*2024)
    stones = new_stones

print(len(stones))