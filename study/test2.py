import sys
# # input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

# 12851

from collections import deque

def bfs1(num):
    global field, visited, k

    visited[num] = 1
    q = deque()
    q.append(num)
    ret = 0

    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if now == k:
                return ret

            for i in (now - 1, now + 1, now * 2):
                if 0 <= i < 200000 and not visited[i]:
                    visited[i] = 1
                    q.append(i)

        ret += 1

def bfs2(num):
    global field, MIN, cnt

    q = deque()
    q.append((num, 0))

    while q:
        now, time = q.popleft()

        if time > MIN:
            continue

        if now == k:
            cnt += 1
            continue

        time += 1
        for i in (now - 1, now + 1, now * 2):
            if 0 <= i <= 200000:
                q.append((i, time))


n, k = map(int, input().split())

field = [0] * 200001
visited = [0] * 200001
MIN = bfs1(n)
cnt = 0
bfs2(n)

print(MIN)
print(cnt)