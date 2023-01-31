import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

col, row = map(int, input().split())
n = int(input())
rows = []
cols = []

for i in range(n):
    a, b = map(int, input().split())
    
    if(a == 0):
        rows += [b]
    else:
        cols += [b]

rows += [row] # 1 1 1 2 2 2 3 3 3 같이 반복해야 한다.
cols += [col] # 1 2 3 1 2 3 1 2 3 같이 반복해야 한다. 2중 반복문을 사용하면 쉽긴하다.
rows = [0] + rows

rows.sort()
cols.sort()

areas = []
for i in range(1, len(rows)):
    top = rows[i - 1]
    left = 0 # 왼쪽 초기값
    for j in range(len(cols)):
        areas += [(rows[i] - top) * (cols[j] - left)] # 세로 * 가로
        left = cols[j] # 갱신

res = max(areas)
print(res)
