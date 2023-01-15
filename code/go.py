# 이름받고 hello, hi, python, world 사전식 정렬 sorted 없이 해보기 17차시
def str_score(s):
    a = len(s)
    lst = []*a

    for i in range(a):
        lst[i] = ord(s[i])
    
    return lst

def bubble_seq(a):
    lst = a
    length = len(a) - 1
    k = len(a)
    
    for i in range(length):
        k -= 1
        for j in range(0, k):
            if (lst[j] > lst[j + 1]):
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return (lst)
