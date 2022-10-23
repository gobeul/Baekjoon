### 백준 14503번 - 로봇 청소기

> 2022/10/23 <br>
> 문제 지문을 이해하는데 좀 애먹었던문제..

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def rotate(pi, pj, d): # 청소후 이동
    global ans
    if not clean[pi][pj]:
        clean[pi][pj] = True
        ans += 1

    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        mi, mj = pi+delta[d][0], pj+delta[d][1]
        if not clean[mi][mj] :
            rotate(mi, mj, d)
            break
    else: # 후진
        back= d - 2 
        if back < 0:
            back += 4
        mi, mj = pi+delta[back][0], pj+delta[back][1]
        if arr[mi][mj] != 1:
            rotate(mi, mj, d) # 후진 시에 방향유지 필요
        

delta = [(-1,0), (0,1), (1,0), (0,-1)] # 북, 동, 남, 서

N, M = map(int, input().split())
pi, pj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clean = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            clean[i][j] = True

ans = 0
rotate(pi, pj, d)

print(ans)
```