import sys
sys.stdin = open("input.txt", "r")

def dfs(level):
    global n, cnt, visited

    if level == n:
        cnt += 1
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(level + 1)
            visited[i] = 0


n = int(input())
visited = [0] * n
cnt = 0

dfs(0)
print(cnt)

