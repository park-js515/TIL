import sys
# # input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

#1211 [S/W 문제해결 기본] 2일차 - Ladder2
def move(row, col, n):
    d = [
        [1, 0], # 아래
        [0, -1], # 왼쪽
        [0, 1] # 오른쪽
    ]

    go = n

    if n == 0:
        for i in [1, 2]:
            drow, dcol = row + d[i][0], col + d[i][1]

            if 0 <= drow < 100 and 0 <= dcol < 100:
                if lst[drow][dcol] == 1:
                    go = i
                    break

    else:
        i = 0
        drow, dcol = row + d[i][0], col + d[i][1]
        if 0 <= drow < 100 and 0 <= dcol < 100:
            if lst[drow][dcol] == 1:
                go = i


    drow, dcol = row + d[go][0], col + d[go][1]

    return drow, dcol, go

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    lst = [list(map(int, input().split())) for i in range(100)]
    mi = 21e7
    idx = 0

    for i in range(100):
        temp_cnt = 1
        drow = 0
        dcol = i
        if lst[drow][dcol] != 1:
            continue

        n = 0
        while drow != 99:
            drow, dcol, n = move(drow, dcol, n)
            temp_cnt += 1

        if mi > temp_cnt:
            mi = temp_cnt
            idx = i

    print(f"#{test_case} {idx} {mi}")