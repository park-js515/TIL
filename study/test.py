import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

def merge_sort(s, e):
    if e - s < 1:
        return

    m = int((s + e)/ 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)

    for i in range(s, e + 1):
        tmp[i] = lst[i]
    
    k = s
    idx1 = s
    idx2 = m + 1
    
    while idx1 <= m and idx2 <= e:
        if tmp[idx1] > tmp[idx2]:
            lst[k] = tmp[idx2]
            k += 1
            idx2 += 1
        else:
            lst[k] = tmp[idx1]
            k += 1
            idx1 += 1
        
    while idx1 <= m:
        lst[k] = tmp[idx1]
        k += 1
        idx1 += 1

    while idx2 <= e:
        lst[k] = tmp[idx2]
        k += 1
        idx2 += 1

##############################################
n = int(input())
lst = [0]*(n + 1)
tmp = [0]*(n + 1)

for i in range(1, n + 1):
    lst[i] = int(input())

merge_sort(1, n)

for i in range(1, n + 1):
    print(lst[i])