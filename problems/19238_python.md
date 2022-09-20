### 백준 19238번 - 스타트 택시

> 2022/09/20 <br>
> 최단거리 손님찾는 용, 목적지까지 최단거리 계산용 이렇게 BFS를 2개 만들었다.<br>
> 결국 손님 1명당 BFS를 2번 돌아야 하는데 N 이 최대 20이라서 통과할 수 있었던것 같다.
```python
import sys
input = sys.stdin.readline
from collections import deque

def G_BFS(i, j): # 최단거리 승객찾는 BFS
    global fuel
    if arr[i][j] > 1: # 택시자리에 손님이 있는 경우
        return i, j
    lst = [] # 최단거리 승객리스트
    visited = [[False]*N for _ in range(N)]
    queue = deque([(i, j, 0)]) # 좌표, 출발점에서 거리
    visited[i][j] = True
    min_dis = 99999999 # 최소거리
    while queue:
        ni, nj, dis = queue.popleft()
        for di, dj in delta:
            mi, mj = ni+di, nj+dj
            # print(mi, mj, visited[mi][mj], arr[mi][mj])
            if 0 <= mi < N and 0 <= mj < N and not visited[mi][mj] and arr[mi][mj] != 1:
                if arr[mi][mj] > 0 : # 승객이 있으면
                    min_dis = dis+1
                    lst.append((mi,mj,min_dis))
                    visited[mi][mj] = True
                    # append 할 필요 없음 쵠단 거리 손님 찾는 거니깐
                else:
                    if dis+1 <= min_dis : # 최단 거리 넘어가면 추가할 큐에 필요 없음
                        queue.append((mi, mj, dis+1))
                        visited[mi][mj] = True

    if lst == []: # 승객을 태울 수 없을때 (테케 3번)
        print(-1)
        quit()

    lst.sort(key=lambda x : (x[2], x[0], x[1])) # 거리, 행, 열 순으로 정렬
    fuel -= lst[0][2] # 연료 감소

    return lst[0][0], lst[0][1]

def D_BFS(i, j): # 승객을 목적지까지 최단거리로 운송하기
    global next_i, next_j
    ep = (guest[arr[i][j]-5][2], guest[arr[i][j]-5][3]) # arr[i][j] 값에 -5를 하면 guest 인덱스가 나옴.
    next_i, next_j = ep
    visited = [[False]*N for _ in range(N)]
    queue = deque([(i, j, 0)]) # 좌표, 출발점에서 거리
    visited[i][j] = True
    while queue:
        ni, nj, dis = queue.popleft()
        for di, dj in delta:
            mi, mj = ni+di, nj+dj
            if 0 <= mi < N and 0 <= mj < N and not visited[mi][mj] and arr[mi][mj] != 1:
                if (mi, mj) == ep:
                    return dis+1 # 사용한 목적지 리턴
                else:
                    queue.append((mi, mj, dis+1))
                    visited[mi][mj] = True

    print(-1) # 목적지에 못가는 경우
    quit()

delta = [(0,1), (0,-1), (1,0), (-1,0)]
## N 이 최대 20이라서 BFS 계속 돌리기에 부담이 적음
N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))

guest = []
for i in range(M):
    a, b, c, d = map(int, input().split())
    arr[a-1][b-1] = 5+i # 승객 표시 (최단거리 승객 찾을때 사용), 나중에 인덱스로 접근할 꺼임
    guest.append((a-1,b-1,c-1,d-1)) # 죄표 표시가 불친절하군

cnt = 0
si, sj = start[0]-1, start[1]-1
while cnt != M:
    i, j = G_BFS(si, sj)
    use_fuel = D_BFS(i, j)

    fuel -= use_fuel
    if fuel < 0:
        print(-1)
        quit()
    else:
        cnt += 1
        fuel += 2*(use_fuel)
        arr[i][j] = 0
        si, sj = next_i, next_j

print(fuel)
```