### 백준 5212번 - 지구 온난화

> 2022/10/05 <br>
> 어렵지 않은 문제임에 문제조건에 '지도 외의 범위는 모두 바다 이다' 라는 부분을 놓쳐서 디버깅하는데 꽤나 애먹었던 문제이다.<br>
> 문제 조건을 .잘. .읽. .자.

```python
import sys
input = sys.stdin.readline

def check(i,j):
    cnt = 0
    for di, dj in delta:
        di += i
        dj += j
        if di < 0 or dj < 0 or N == di or M == dj or arr[di][dj] == '.':
            cnt += 1

    if cnt >= 3:
        submerge.add((i,j))

delta = [(0,1), (0,-1), (1,0), (-1,0)]

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

submerge = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            check(i,j)

for i, j in submerge:
    arr[i][j] = '.'

si, sj, ei, ej = 9999, 9999, -1, -1 # 
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            si, sj = min(i, si), min(j, sj)
            ei, ej = max(i, ei), max(j, ej)

for lst in arr[si:ei+1]:
    s = "".join(lst[sj:ej+1])
    print(s)
```