import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

n = int(input())
res = []
lst = []
k = 1
tf = True

for i in range(n):
    now = int(input())

    if k <= now:
        while k <= now:
            lst.append(k)
            res.append('+')
            k += 1
 
        lst.pop()
        res.append('-')

    elif k > now:
        a = lst.pop()
        res.append('-')
        if a != now:
            tf = False
            break

if tf:
    for i in res:
        print(i)
else:
    print("NO")