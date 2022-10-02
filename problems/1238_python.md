### 백준 1238번 - 파티

> 2022/10/02 <br>
> N개의 집이 있을때 N-1개의 집에서 X까지 다익스트라 N번, X 에서 N개의 집까지 다익스트라 1번<br>
> 이렇게 총 N 번의 다익스트라를 돌려야 된다고 생각 할 수 있지만<br>
> 집에서 x를 x에서 집으로 바꾸면 총 다익스트라 2번으로 가능하다.

```python
import sys
input = sys.stdin.readline
import heapq

def dijkstra_toX():
    que = []
    heapq.heappush(que, (0, X))

    while que:
        dis, node = heapq.heappop(que)
        if dis_lst_toX[node] < dis:
            continue
        for next_dis, next in graph_toX[node]:
            tmp = dis + next_dis
            if tmp < dis_lst_toX[next]:
                dis_lst_toX[next] = tmp
                heapq.heappush(que, (tmp, next))

def dijkstra_toHome():
    que = []
    heapq.heappush(que, (0, X))

    while que:
        dis, node = heapq.heappop(que)
        if dis_lst_toHome[node] < dis:
            continue
        for next_dis, next in graph_toHome[node]:
            tmp = dis + next_dis
            if tmp < dis_lst_toHome[next]:
                dis_lst_toHome[next] = tmp
                heapq.heappush(que, (tmp, next))
    
        
"""
모든 집에서 파티 장소로 가야한다. 
다익스트라를 N-1 번 돌리는 것보다
X 에서 출발하는 방법으로 계산해보자.
"""

N, M, X = map(int, input().split()) # N ; 학생 수, M ; 경로수, X 파티 장소

graph_toX = [[] for _ in range(N+1)] # 1 번 ~ N 번
graph_toHome = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph_toX[e].append((d, s)) # X에서 출발이기 때문에 방향을 반대로 잡아 준다.
    ## 힘큐를 사용하기 위헤 거리정보를 첫번째 인덱스로
    ### 거꾸로 연결해서 X기준으로 출발점을 잡아주면 N 번에서 X까지의 최단거리를 다익 1번으로 구할 수 있다.

    graph_toHome[s].append((d, e)) # 정방향 으로 잡아준다.
    # X에서 집까지의 최단거리를 위해


inf = 99999999
dis_lst_toX = [inf]*(N+1)
dis_lst_toX[X] = 0

dis_lst_toHome = [inf]*(N+1)
dis_lst_toHome[X] = 0

dijkstra_toX() # 집에서 X 까지의 최단거라
dijkstra_toHome() # X 에서 집까지의 최단거리

ans = 0
for i in range(1, N+1):
    tmp = dis_lst_toX[i] + dis_lst_toHome[i]
    ans = max(ans, tmp)

print(ans)
```