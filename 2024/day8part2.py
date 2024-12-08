from math import sqrt

ans = 0

m = open(0).read().splitlines()

rows = len(m)
cols = len(m[0])

antennas = {}

def dist(p1, p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def calc_slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

def on_same_line(m, p1, p2):
    return p1[1] - p2[1] == m * (p1[0] - p2[0])

for i, line in enumerate(m):
    for j, c in enumerate(line):
        if c.isalnum():
            if antennas.get(c) == None:
                antennas[c] = list()
            antennas[c].append((j, i))

antinodes = set()
for i in range(rows):
    for j in range(cols):
        for freq_gp in antennas:
            for k, point1 in enumerate(antennas[freq_gp]):
                for point2 in antennas[freq_gp][k+1:]:
                    if on_same_line(calc_slope(point1, point2), point2, (j, i)):
                        antinodes.add((j,i))

print(len(antinodes))

# for i, line in enumerate(m):
#     for j, c in enumerate(line):
#         if not c.isalnum() and (j,i) in antinodes:
#             print('#', end='')
#         else:
#             print(c, end='')
#     print()
