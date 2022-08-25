### 백준 17141번 - 연구소 2

> 2022/08/25 <br>
> BFS 바탕에 시작점의 최적의 배치를 고민해야 되는 문제이다<br>
> 최적의 시작점을 배치하는 아이디어가 떠오르지 않아 부분집합으로 모든 경우의 수를 다 구해 비교해 봤는데 의외로 시간초과는 나오지 않았다.

```python
import copy

N, M = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N) ]
ori_visited = [[False]*N for _ in range(N)] # 방문기록 원본
delta = [(-1,0), (1,0), (0,-1), (0,1)] # 델타

visit_cnt = N*N # 방문해야될 곳
st_p = [] # 바이러스 가능 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1: # 벽
            ori_visited[i][j] = True
            visit_cnt -= 1 # 벽일 때만 빼준다.
        elif arr[i][j] == 2:
            st_p.append((i,j))


checking = False # 올 감염이 가능한 경우가 있는가?
cc = len(st_p)
combi = [] # 조합 가능한 경우의 수 집합
# 조합 가능한 경우 
for i in range(1<<cc):
    tmp = []
    for j in range(cc):
        if i & (1<<j):
            tmp.append(j)
    if len(tmp) == M:
        combi.append(tmp)

ans = [] # 모든 경우의 day가 들어갈 리스트
for case in combi:
    visited = copy.deepcopy(ori_visited) # 방문기록, 큐 초기화
    Queue = [] # BFS 쓸껀데 어짜피 tmp 만들어서 매번 pop으로 다 빼주기 때문에 deque할 필요는 없습니다.
    vcnt = visit_cnt
    for i in case: # 시작점 작업
        si, sj = st_p[i]
        Queue.append((si,sj))
        visited[si][sj] = True
        vcnt -= 1 

    #BFS 시작
    sec = -1
    while Queue:
        sec += 1
        tmp = Queue[:]
        Queue = []
        while tmp:
            sti, stj = tmp.pop()
            for di, dj in delta:
                mi = sti + di
                mj = stj + dj

                # 인덱스범위 + 비방문
                if 0<=mi<N and 0<=mj<N and visited[mi][mj] == False:
                    visited[mi][mj] = True
                    Queue.append((mi,mj))
                    vcnt -= 1

    if vcnt == 0 : # 다방문했으면
        checking = True
        ans.append(sec)

if checking : # 올 감염할 수 있는 경우가 1개라도 있으면
    print(min(ans))
else:
    print(-1)
```