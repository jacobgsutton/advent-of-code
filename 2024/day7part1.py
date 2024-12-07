ans = 0

eqs_in = open(0)
eqs = list()

for eq in eqs_in:
    lhs, rhs = eq.split(': ')
    eqs.append((int(lhs), list(map(int, rhs.split(' ')))))

for eq in eqs:
    b = 2**(len(eq[1])-1)
    for x in range(b):
        rhs = eq[1][0]
        for i in range(1, len(eq[1])):
            if x & (1<<(i-1)):
                rhs *= eq[1][i]
            else:
                rhs += eq[1][i]
        if rhs == eq[0]:
            ans += rhs
            break
print(ans)