import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline
from collections import deque
n = int(input())
data = deque()

for i in range(1, n + 1):
    data.append(i)

for i in range(n - 1):
    data.popleft()
    data.append(data.popleft())

# while len(data) > 1:
#     data.popleft()
#     data.append(data.popleft())


print(*data)
