### 백준 14502번 - 연구소

> 2022/09/30 <br>
> 조합 + BFS + 백트래킹 구현 문제 였다. 별다른 어려움은 없었다.<br>
> 단지 리스트 값의 변경이 아닌 단순 pop만 할 경우에도 리스트의 얕은복사가 필요하다는 점을 간과했었다.

```python
import sys
sys.stdin = open("eee.txt", "r")
input = sys.stdin.readline

def recur(s, lst, last): # 3개 뽑는 조합 구하기
    if s == 3:
        combi.append(lst)
        return
    
    for i in range(last, blank_cnt):
        recur(s+1, lst+[i], i+1)

def BFS():
    visited = [[False]*(M) for _ in range(N)]
    stack = virus[:] # 얕은 복사 필수! 단순 pop() 도 영향을 준다
    for i, j in stack:
        visited[i][j] = True

    safe_area = safe
    while stack:
        i, j = stack.pop()
        for di, dj in delta:
            mi, mj = i+di, j+dj
            if 0 <= mi < N and 0 <= mj < M and not visited[mi][mj] and not arr[mi][mj]:
                visited[mi][mj] = True
                stack.append((mi, mj))
                safe_area -= 1
                if safe_area <= ans:
                    return -1

    return safe_area


delta = [(0,1), (0,-1), (1,0), (-1,0)]
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

blank, virus, safe = [], [], 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i,j)) # 빈칸 좌표 추가
            safe += 1
        elif arr[i][j] == 2:
            virus.append((i,j)) # 바이러스 좌표추가


safe -= 3 # 무조건 3개의 벽을 세워야함

blank_cnt = len(blank)
tmp = [i for i in range(blank_cnt)]
visited = [False]*(blank_cnt)
combi = [] # 조합들 추가되는 곳

recur(0, [], 0)
ans = 0
for lst in combi:
    for k in lst:
        i, j = blank[k]
        arr[i][j] = 1 # 벽 세워 보고

    tmp = BFS()
    ans = max(ans, tmp)

    for k in lst:
        i, j = blank[k]
        arr[i][j] = 0 # 벽 철회


print(ans)
```