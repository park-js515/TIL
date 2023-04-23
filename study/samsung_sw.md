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

### 14499 주사위 굴리기

```py
import sys
input = sys.stdin.readline

dice = [0, 0, 0, 0, 0, 0, 0] # 주사위의 값
dice_pos = [0, 1, 2, 3, 4, 5, 6] # top, n, e, w, s, bot

# 주사위가 좌우로 움직이면 북남은 고정, 나머지는 순회
target_12 = [1, 3, 6, 4]
target_1 = [1, 2, 3, 0]
target_2 = [3, 0, 1, 2]
# 주사위가 북남으로 움직이면 동서는 고정, 나머지는 순회
target_34 = [1, 5, 6, 2]
target_3 = [1, 2, 3, 0]
target_4 = [3, 0, 1, 2]

d = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))
n, m, r, c, k = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
commands = tuple(map(int, input().split()))

row = r
col = c
for comm in commands:
    drow = row + d[comm][0]
    dcol = col + d[comm][1]

    if 0 <= drow < n and 0 <= dcol < m:
        temp = [0] * 4

        if comm in (1, 2):
            for i in range(4):
                temp[i] = dice[target_12[i]]

            if comm == 1:
                for i in range(4):
                    dice[target_12[i]] = temp[target_1[i]]
            else:
                for i in range(4):
                    dice[target_12[i]] = temp[target_2[i]]

        else:
            for i in range(4):
                temp[i] = dice[target_34[i]]

            if comm == 3:
                for i in range(4):
                    dice[target_34[i]] = temp[target_3[i]]
            else:
                for i in range(4):
                    dice[target_34[i]] = temp[target_4[i]]

        if field[drow][dcol] == 0:
            field[drow][dcol] = dice[6]
        else:
            dice[6] = field[drow][dcol]
            field[drow][dcol] = 0

        row = drow
        col = dcol
        print(dice[1])
```

&nbsp;

### 다음 문제

```
```

&nbsp;

