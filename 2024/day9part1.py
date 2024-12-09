ans = 0

m = open(0).read().strip()

d = []
n = 0
block_ends = []
for i, c in enumerate(m):
    if i % 2 == 0:
        d.extend(str(n) for _ in range(int(c)))
        n+=1
        if i == len(m)-1:
            block_ends.append(len(d))
    elif int(c) != 0:
        block_ends.append(len(d))
        d.extend('.' for _ in range(int(c)))

i = 0
j = len(block_ends)-1
l_pos = block_ends[i]
r_pos = block_ends[j]

while l_pos < r_pos-1:
    #print(','.join(d))
    d[l_pos]=d[r_pos-1]
    d[r_pos-1]='.'
    if d[l_pos+1] == '.': l_pos += 1
    else:
        l_pos = block_ends[i+1]
        i+=1
    if d[r_pos-2].isnumeric(): r_pos -= 1
    else:
        r_pos = block_ends[j-1]
        j-=1

# print('finial', ','.join(d))

for i, id in enumerate(d):
    if id == '.': break
    ans += i * int(id)
print(ans)