import sys
# # input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

# 12851

from collections import deque
def bfs(num):
    global k, visited, res

    visited[num] = 0
    q = deque()
    q.append(num)
    cnt = 0

    while q:
        now = q.popleft()

        if visited[now] >= visited[k]:
            continue

        for i in [now - 1, now + 1, now * 2]:
            if 0 <= i <= 101000:
                if visited[i] >= visited[now] + 1:
                    visited[i] = visited[now] + 1

                    if i != k:
                        q.append(i)
                    else:
                        res += 1


n, k = map(int, input().split())

if n >= k:
    print(n - k)
    print(1)
else:
    visited = [21e8] * 101001
    res = 0
    bfs(n)

    print(visited[k])
    print(res)