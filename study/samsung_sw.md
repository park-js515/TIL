# 삼성 소프트웨어 역량 테스트 기출 문제

### 14502 연구소 (Gold4)

```py
import sys
input = sys.stdin.readline
from collections import deque


def COPY(now_field): # deepcopy 할 때는 사용자 정의함수를 사용하는 것이 더 빠르다.
    global n, m

    temp_field = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp_field[i][j] = now_field[i][j]

    return temp_field


def bfs(now_field):
    global n, m, virus

    q = deque(virus)
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while q:
        row, col = q.popleft()

        for i in range(4):
            drow = row + d[i][0]
            dcol = col + d[i][1]

            if 0 <= drow < n and 0 <= dcol < m:
                if now_field[drow][dcol] == 0:
                    now_field[drow][dcol] = 2
                    q.append((drow, dcol))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if now_field[i][j] == 0:
                cnt += 1

    return cnt


def dfs(r, c, level):
    global n, m, field, MAX

    if level == 3:
        temp_field = COPY(field)
        MAX = max(MAX, bfs(temp_field))
        return

    for i in range(r, n):
        for j in range(m):
            if i == r and j < c:
                continue

            if field[i][j] == 0:
                field[i][j] = 1
                dfs(i, j + 1, level + 1)
                field[i][j] = 0


n, m = map(int, input().split())
field = []
virus = []

for i in range(n):
    temp = list(map(int, input().split()))
    field.append(temp)

    for j in range(m):
        if temp[j] == 2:
            virus.append((i, j))

MAX = 0
dfs(0, 0, 0)
print(MAX)
```
&nbsp;

### 다음 문제

```
```

&nbsp;

