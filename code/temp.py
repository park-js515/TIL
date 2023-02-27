# import sys
# sys.stdin = open("input.txt", "r")

mi = 21e8
def dfs(level, s):
    global mi, lst1, lst2, visited1, visited2

    if level == 12:
        if abs(mi) > abs(s):
            mi = s
        return

    if level % 2:
        for i in range(6):
            if not visited2[i]:
                visited2[i] = 1
                dfs(level + 1, s +  lst2[i] * (level + 1))
                visited2[i] = 0
    else:
        for i in range(6):
            if not visited1[i]:
                visited1[i] = 1
                dfs(level + 1, s + lst1[i] * (level + 1))
                visited1[i] = 0



lst1 = [-2, 3, 4, 9, -5, 2]
lst2 = [4, 7, -3, -6, -1, 2]
visited1 = [0] * 6
visited2 = [0] * 6

dfs(0, 0)
print(mi)