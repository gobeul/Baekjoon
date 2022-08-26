### 백준 17142번 - 연구소 3

> 2022/08/26 <br>
> 17141번과 조건만 살짝 다르고 같은 문제였다. 17141번은 바이러스를 두지 않은 곳은 빈곳(0)이었지만 이문제는 비활성화 바이러스라면 퍼지지만 않을뿐 바이러스 자리(2)로 인식된다.

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
            visit_cnt -= 1 # 비활성 바이러스도 바이러스 취급이라 있는거 다 뺴준다. 17141번과 다른 부분

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

if visit_cnt == 0: # 처음부터 빈곳이 없는 경우
    print(0)
    quit()

ans = [] # 모든 경우의 day가 들어갈 리스트
for case in combi:
    visited = copy.deepcopy(ori_visited) # 방문기록, 큐 초기화
    Queue = [] # BFS 쓸껀데 어짜피 tmp 만들어서 매번 pop으로 다 빼주기 때문에 deque할 필요는 없습니다.
    vcnt = visit_cnt
    for i in case: # 시작점 작업
        si, sj = st_p[i]
        Queue.append((si,sj))
        visited[si][sj] = True
        # vcnt -= 1 17141번과 다른 부분


    #BFS 시작
    sec = 0 # 17141번과 다른 부분 종료조건이 17141과 다르게 개수를 카운트해서 break 로 나오기 때문에 큐가 비어있게 되는 검증을 진행하지 않는다 0부터 시작
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
                    if (mi, mj) not in st_p: # 17141번과 다른 부분
                        vcnt -= 1

        if vcnt == 0 : # 다방문했으면 // 17141번과 다른 부분 들여쓰기 되어 있고 브래이크추가
            checking = True
            ans.append(sec)
            break
if checking : # 올 감염할 수 있는 경우가 1개라도 있으면
    print(min(ans))
else:
    print(-1)
```