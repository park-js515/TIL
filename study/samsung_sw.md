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

### 14499 주사위 굴리기 (Gold4)

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

### 17143 낚시왕

```py
import sys
input = sys.stdin.readline


def COPY(lst):
    lg = len(lst)
    ret = [[] for _ in range(lg)]

    for i in range(lg):
        ret[i] = lst[i][:]

    return ret


R, C, M = map(int, input().split())
sharks = [[] for _ in range(M)]
res = 0
INF = int(21e8)
D = ((0, 0), (-1, 0), (1, 0), (0, 1), (0, -1))
chg = {1: 2, 2: 1, 3: 4, 4: 3}

R_cycle = 2 * (R - 1)
C_cycle = 2 * (C - 1)

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or d == 2:
        s %= R_cycle
    else:
        s %= C_cycle

    sharks[i] = [r, c, s, d, z]

for i in range(1, C + 1):
    idx = -1
    MIN = INF
    temp = 0

    if not sharks:
        break

    for j in range(len(sharks)):
        r, c, s, d, z = sharks[j]

        if i == c:
            if MIN > r:
                idx = j
                MIN = r

    if idx != -1:
        r, c, s, d, z = sharks.pop(idx)
        res += z

    for j in range(len(sharks)):
        r, c, s, d, z = sharks[j]

        drow = r
        dcol = c

        if d == 1 or d == 2:
            drow = r + D[d][0] * s

            for _ in range(2):
                if drow < 1:
                    drow = 2 - drow
                    d = chg.get(d)
                elif drow > R:
                    drow = 2 * R - drow
                    d = chg.get(d)
                else:
                    break
        else:
            dcol = c + D[d][1] * s

            for _ in range(2):
                if dcol < 1:
                    dcol = 2 - dcol
                    d = chg.get(d)
                elif dcol > C:
                    dcol = 2 * C - dcol
                    d = chg.get(d)
                else:
                    break

        sharks[j] = [drow, dcol, s, d, z]


    if not sharks:
        break

    sharks.sort(key = lambda x: (x[0], x[1]))
    nxt_sharks = []

    r, c, s, d, z = sharks[0]
    tf = False

    for j in range(1, len(sharks)):
        x1, x2, x3, x4, x5 = sharks[j]


        if r == x1 and c == x2:
            if z < x5:
                r, c, s, d, z = x1, x2, x3, x4, x5
        else:
            nxt_sharks.append([r, c, s, d, z])
            r, c, s, d, z = x1, x2, x3, x4, x5

            if j == len(sharks) - 1:
                tf = True

    if len(sharks) > 1:
        if tf:
            nxt_sharks.append([x1, x2, x3, x4, x5])
        else:
            nxt_sharks.append([r, c, s, d, z])
    else:
        nxt_sharks.append([r, c, s, d, z])

    sharks = COPY(nxt_sharks)

print(res)
```

&nbsp;

### 1520 내리막 길

DFS + DP or BFS + priority queue로 풀 수 있다는데...?

```py
def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for (nx, ny) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if 0 > nx or nx >= N or 0 > ny or ny >= M:
            continue
        if m[y][x] > m[ny][nx]:
            dp[y][x] += dfs(nx, ny)
    return dp[y][x]

M, N = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
print(dfs(0, 0))
```

&nbsp;

### 다음 문제

```
```

&nbsp;