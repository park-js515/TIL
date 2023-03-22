import sys
# # input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

# 12851

from collections import deque

def bfs(num):
    global visited, v, n, k

    visited[num] = 1
    q = deque()
    q.append(num)

    while q:
        now = q.popleft()

        for i in (now - 1, now + 1, now * 2):
            if 0 <= i <= 100000:
                if not visited[i]:
                    visited[i] = visited[now] + 1
                    q.append(i)
                    v[i] = now

                    if i == k:
                        time = visited[k] - 1
                        lst = []

                        while i != n:
                            lst.append(i)
                            i = v[i]

                        lst.append(n)
                        lst.reverse()

                        return time, lst


n, k = map(int, input().split())

if n >= k:
    time = n - k
    lst = list(range(n, k - 1, -1))
else:
    visited = [0] * 100001
    v = [0] * 100001
    time, lst = bfs(n)

print(time)
print(*lst)