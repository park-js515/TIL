import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

def chg(ch):
    chg1 = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    return chg1[ch]

def compare(cnt, restrict):
    ret = [0]*4
    
    for i in range(4):
        if cnt[i] >= restrict[i]:
            ret[i] += 1

    return ret

def step(ch, i):
    global st, cnt, restrict, check

    # minus
    a = st[i - 1]
    idx1 = chg(a)
    cnt[idx1] -= 1

    if cnt[idx1] < restrict[idx1] and check[idx1] == 1:
        check[idx1] -= 1

    # plus
    idx2 = chg(ch)
    cnt[idx2] += 1

    if cnt[idx2] >= restrict[idx2] and check[idx2] == 0:
        check[idx2] += 1


s, p = map(int, input().split())
st = list(input())
restrict = list(map(int, input().split())) # A C G T
cnt = [0] * 4
res = 0

temp = st[0:p]
for i in temp:
    cnt[chg(i)] += 1

check = compare(cnt, restrict)
if sum(check) == 4:
    res += 1

for i in range(1, s - p + 1):
    step(st[p - 1 + i], i)

    if sum(check) == 4:
        res += 1

print(res)