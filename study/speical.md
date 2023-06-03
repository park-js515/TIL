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

### lazy propagation  

기존에 내가 풀던 방식을 사용하면 메모리 측면, 속도 측면에서 문제가 발생한다.
이를 보고 나중에 반영할 수 있도록 하자.

```py
import math
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    update_range(tree, lazy, node*2, start, (start+end)//2, left, right, diff)
    update_range(tree, lazy, node*2+1, (start+end)//2+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, lazy, node, start, end, left, right):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, lazy, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, lazy, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
lazy = [0] * tree_size
m += k
init(a, tree, 1, 0, n-1)
print(tree)
for _ in range(m):
    what, *q = map(int, input().split())
    if what == 1:
        left, right, diff = q
        update_range(tree, lazy, 1, 0, n-1, left-1, right-1, diff)
    else:
        left, right = q
        print(query(tree, lazy, 1, 0, n-1, left-1, right-1))
```