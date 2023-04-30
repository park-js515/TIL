# 모르면 못푸는 알고리즘 모음

### 페르마의 소정리  

when p is Prime_Number  

$$a^{p} \equiv a (mod \; p)$$
$$a^{p-2} \equiv a^{-1} (mod \; p)$$

```py
# 백준 11401 이항 계수 3
# 백준 16134 조합(Combination)
# 페르마의 소정리

n, k = map(int, input().split())
MOD = 1000000007

ans = 1
for i in range(k + 1, n + 1):
    ans = ans * i % MOD

A = 1
for i in range(1, n - k + 1):
    A = A * i % MOD

e = MOD - 2

while e:
    if e & 1:
        ans = ans * A % MOD
    e >>= 1
    A = A * A % MOD

print(ans)
```

### 분할정복  

python의 pow 함수는 분할 곱을 제공한다.  

```py
# https://www.acmicpc.net/problem/15824

n = int(input())
lst = sorted(map(int, input().split()))
ans = 0

MOD = 1000000007
for i, x in enumerate(lst):
    ans = (ans + x * (pow(2, i, MOD) - pow(2, n - i - 1, MOD))) % MOD

print(ans)
```