import sys
sys.stdin = open("input.txt", "r")

n = int(input())
lst = list(map(int, input().split()))
res = []

for i in range(len(lst)):
    ch = 