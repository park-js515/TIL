import sys
sys.stdin = open("input.txt", "r")

# 1244

# import sys
# input = sys.stdin.readline

# 1244

def ftn(lst, r, a, b):
    ret = lst[:]
    
    def cng(k):
        return k * (-1) + 1
    
    bot, top = 1, r

    if (a == 1):
        for i in range(b, r + 1, b):
            ret[i] = cng(ret[i])
    
    if (a == 2):
        ret[b] = cng(ret[b])
        left = b - 1
        right = b + 1

        while (left >= bot and right <= top):
            if (ret[left] == ret[right]):
                ret[left], ret[right] = cng(ret[left]), cng(ret[right])
                left -= 1
                right += 1
            else:
                break

    return ret

r = int(input())
lst = list(map(int, input().split()))
lst = [0] + lst
n = int(input())

for i in range(n):
    a, b = map(int, input().split()) # 성별, 번호
    lst = ftn(lst, r, a, b)

lst = lst[1:]

# 20개씩 출력하기
k = 0
while (k + 20 < r):
    print(*lst[k:k + 20])
    k += 20

print(*lst[k:])