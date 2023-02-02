import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

# 2578
# 2477 참외밭

def ftn(start, a, b): # 동서남북
    x = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

    temp = x[a - 1]
    move = [temp[0] * b, temp[1] * b]
    ret = [start[0] + move[0], start[1] + move[1]]

    return ret


def ftn2(lst):
    row = []
    col = []

    for i in lst:
        a = i[0]
        b = i[1]

        if a not in row:
            row.append(a)
        if b not in col:
            col.append(b)

    return (row, col)


def ftn3(m):
    for i in range(2):
        k1 = m[i]
        for j in range(1, 3):
            if k1[0] != m[j][0]:
                if k1[1] != m[j][1]:
                    k2 = m[j]
                    return k1, k2


def bubble(lst):
    temp = lst[:]
    lg = len(temp)

    for i in range(lg - 1):
        for j in range(lg - 1 - i):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]

    return temp

##################################################################

val = int(input())
start = [0, 0]
point = []

for i in range(6):
    a, b = map(int, input().split())
    temp = ftn(start, a, b)
    point.append(temp)
    start = temp

rows, cols = ftn2(point)
rows = bubble(rows)
cols = bubble(cols)
mr = rows[1]
mc = cols[1]

m = []

for i in point:
        if i[0] == mr and i not in m:
            m.append(i)
        
        if i[1] == mc and i not in m:
            m.append(i)


k1, k2 = ftn3(m)


total = (rows[2] - rows[0]) * (cols[2] - cols[0])
fraction = (k1[0] - k2[0]) * (k1[1] - k2[1]) if ((k1[0] - k2[0]) * (k1[1] - k2[1]) > 0) else -((k1[0] - k2[0]) * (k1[1] - k2[1]))
ret = (total - fraction) * val

print(ret)
