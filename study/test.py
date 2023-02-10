import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

def my_quick(lst):
    def sort(start, end):
        if start >= end:
            return
        
        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)

    def partition(start, end):
        pivot = lst[(start + end) // 2]
        while start <= end:
            while lst[start] < pivot:
                start += 1

            while lst[end] > pivot:
                end -= 1
        
            if start <= end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1

        return start

    return sort(0, len(lst) - 1)

lst = [3, 1, 2, 4, 5]
my_quick(lst)
print(lst)