import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

# 2304
n = int(input())
max_height = 0
max_point = None
lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])
    if (b > max_height):
        max_height = b
        max_point = a

lst2 = sorted(lst, key = lambda x: x[0])
mi = lst2[0][0]
ma = lst2[-1][0]
field = [[0]*(ma + 1) for i in range(max_height + 1)]

for i in lst2:
    if (i[0] < max_point):
        for j in range(i[1]):
            for k in range(i[0], max_point + 1):
                field[j][k] = 1
    else:
        for j in range(i[1]):
            for k in range(max_point, i[0] + 1):
                field[j][k] = 1


res1 = list(map(sum, field))
res2 = sum(res1)

print(res2)