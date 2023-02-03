import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

# 2527 직사각형
def absol(n):
    if n < 0:
        return -n
    else:
        return n


def far(lst):
    a = lst[:2]
    b = lst[2:4]
    c = lst[4:6]
    d = lst[6:]

    ma = 0
    p1 = None
    p2 = None
    for i in [a, b]:
        for j in [c, d]:
            temp = absol(i[0] - j[0]) + absol(i[1] - j[1])  # manhatan distance
            if temp > ma:
                ma = temp
                p1, p2 = i, j

    return (p1, p2)


# def lin(lst):
#     a = lst[:2]
#     b = lst[2:4]
#     c = lst[4:6]
#     d = lst[6:]

#     l11 = absol(a[0] - b[0])
#     l12 = absol(a[1] - b[1])
#     l21 = absol(c[0] - d[0])
#     l22 = absol(c[1] - d[1])

#     return l11, l12, l21, l22


###################################################################
for i in range(4):
    lst = list(map(int, input().split()))
    p1, p2 = far(lst)

    print(f"#{i}: {p1}, {p2}")



    # print(f"#{i}: {p1}, {p2}")
    # print(f"#{i}: {p1w}, {p1h}, {p2w}, {p2h}")