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