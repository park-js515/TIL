import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

# 2578
def bingo(lst):
    cnt = 0

    temp_cnt = 0
    for i in range(5):
        if lst[i][i] == 0:
            temp_cnt += 1
    
    if temp_cnt == 5:
        cnt += 1

    temp_cnt = 0
    for i in range(5):
        if lst[i][4 - i] == 0:
            temp_cnt += 1

    if temp_cnt == 5:
        cnt += 1

    for i in range(5):
        if lst[i] == [0]*5:
            cnt += 1

    for i in range(5):
        temp_cnt = 0
        for j in range(5):
            if lst[j][i] == 0:
                temp_cnt += 1
        
        if temp_cnt == 5:
            cnt + 1

    return cnt


lst = [list(map(int, input().split())) for i in range(5)]
go = [list(map(int, input().split())) for i in range(5)]
go = sum(go, [])

n = 0
num = go[n]

while (bingo(lst) < 3):
    for i in range(5):
        for j in range(5):
            if lst[i][j] == num:
                lst[i][j] = 0
    
    n += 1

print(1)
