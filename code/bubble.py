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

# print(bubble_seq([1, 9, 5, 4, 2, 1]))

# print(bubble_seq([1000, -1, 123, 25, 30, -30, 5]))

# print(bubble_seq(["hello", "hi", "python", "world"]))

## 스트링의 아스키 코드값 반환받기
def str_score(s):
    a = len(s)
    lst = [0]*a

    for i in range(a):
        lst[i] = ord(s[i])
    
    return lst

## 정렬 (불완전?)
def str_compare(s1, s2):
    s11 = s1 + " "
    s21 = s2 + " "

    k = 0
    ret = [s1, s2]
    while(True):
        if (s11 > s21):
            ret = [s2, s1]
            break;
        if (s11 < s21):
            break;
        if ((k + 1) == len(s11) or (k + 1) == len(s21)):
            break;
    
    return(ret)

str_compare("hello", "asdf")


# 선택정렬

# for i in range(len(lst2)):
#     m = lst2[i]
#     idx = i
#     for j in range(i+1, len(lst2)):
#          if (m > lst2[j]):
#             m = lst2[j]
#             idx = j
    
#     if (i != idx):
#         lst2[i], lst2[idx] = lst2[idx], lst2[i]