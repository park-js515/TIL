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
