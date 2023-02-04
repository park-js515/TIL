import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

trs = {0: 5, 1: 3, 2: 4, 3: 5, 4: 2, 5: 0}

def pos(val, lst):
    temp = lst[:]

    for i in range(6):
        if (temp[i] == val):
            break
    
    ret1 = temp[trs[i]]
    temp2 = []
    
    for j in range(6):
        if (j not in [i, trs[i]]):
            temp2.append(temp[j])

    return (ret1, temp2)

n = int(input())
a = list(map(int, input().split()))
lst = [list(map(int, input().split())) for i in range(n - 1)]
result = []


for i in range(6):
    temp = a[:]
    sum_lst = []
    val = temp[i]
    temp2 = []
    
    for j in range(6):
        if (j not in [i, trs[i]]):
            temp2.append(temp[j])
    
    sum_lst.append(temp2)

    for j in lst:
        temp = j[:]
        val, temp = pos(val, temp)
        sum_lst.append(temp)
    
    res1 = list(map(max, sum_lst))
    res2 = sum(res1)
    result.append(res2)

print(result)