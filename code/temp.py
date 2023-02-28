# import sys
# sys.stdin = open("input.txt", "r")

def dfs(level, start):
    global lst, lst2, mi

    if level == 7:
        return

    mi = min(mi, abs(sum(lst) - sum(lst2)))

    for i in range(start, 7):
        lst2[i] = lst[i]
        lst[i] = 0
        dfs(level + 1, i)
        lst[i] = lst2[i]
        lst2[i] = 0

mi = 21e8
lst = [49, 6, 54, 80, 3, 18, 71]
lst2 = [0] * 7

dfs(0, 0)
print(mi)