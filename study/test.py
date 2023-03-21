import sys
sys.stdin = open("input.txt", "r")

import sys
from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        if x == K:
            print(visited[x] - 1)
            ans = []

            while x != N:
                ans.append(x)
                x = v[x]
            ans.append(N)
            ans.reverse()
            print(' '.join(map(str, ans)))
            return

        for i in [x, -1, 1]:
            nx = x + i
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
                v[nx] = x


N, K = map(int, input().split())
visited = [0] * 100001
v = [0] * 100001

bfs(N)

