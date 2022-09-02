### 백준 1654번 - 랜선 자르기

> 2022/09/02 <br>
> 이진탐색 문제..!

```python
import sys
input = sys.stdin.readline

def CNT(L):
    c = 0
    for i in lines:
        c += i // L
    return c

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

s, e = 1, max(lines)
L = (s+e)//2

ans = 0
while s <= e and L != 0:
    if CNT(L) < N:
        e = L-1
        L = (s+e)//2
    else:
        if ans < L:
            ans = L
        s = L+1
        L = (s+e)//2

print(ans)
```