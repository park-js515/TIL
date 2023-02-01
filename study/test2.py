import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

def clr(a, b):
    if (a == 0 or b == 0):
        return a + b
    if (a == b):
        return a
    
    return a + b

T = int(input())    

for test_case in range(1, T + 1):
    n = int(input())
    total = 0

    for i in range(n):
        a, b, c, d, e = map(int, input().split())
        field = [[0]*10 for i in range(10)]

        for j in range(a, c + 1):
            for k in range(b, d + 1):
                field[j][k] = clr(field[j][k], e)

    for j in range(10):
        for k in range(10):
            if (field[j][k] == 3):
                total += 1

    # print(f"#{test_case} {total}")
    print(field)