### 백준 2961번 - 도영이가 만든 맛있는 음식

> 2022/10/13 <br>
> 별다를 점이 없는 조합 문제였던 것 같디.


```python
import sys
input = sys.stdin.readline

def recur(s, lst, last):
    combi.append(lst)

    if s == N:
        return
    
    for i in range(last+1, N):
        recur(s+1, lst+[i], i)

def cooking(lst):
    s, b = 1, 0
    for i in lst:
        s *= S[i]
        b += B[i]
    
    return abs(s-b)

N = int(input())
S, B = [], []
for _ in range(N):
    s, b = map(int, input().split())
    S.append(s)
    B.append(b)

combi = []
recur(0, [], -1)

ans = 9999999999

for lst in combi:
    if lst:
        ans = min(ans, cooking(lst))

print(ans)
```