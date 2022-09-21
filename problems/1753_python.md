### 백준 1753번 - 최단경로

> 2022/09/21 <br>
> 힙을 사용한 다익스트라 구현해보기
> 힙으로 우선순위 큐를 만들어 다익스트라에 적용해야 시간초과를 피할 수 있는 문제였다.<br>
> 아직 우선순위 큐, 힙, 다익스트라가 어떻게 맞물려 돌아가는지 완전히 이해는 못했다.

```python
import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    q = [] # 우선순위 큐(최소힙)
    heapq.heappush(q, (0, start)) # start 노드에 거리 0을 넣는다. 거리 기준으로 자동정렬 되기 위해 거리정보를 0번 인덱스에 넣어준다.
    distance[start] = 0

    while q:
        dis, node = heapq.heappop(q) # 우선 순위 큐에서 뽑음
        if distance[node] < dis:
            continue
        for next, next_dis in graph[node]:
            cost = next_dis + dis
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (next_dis, next))
    
# def smallest_dis(): # 최소거리 찾는게 필요 없어짐. -> 시간 복잡도 감소
#     minV = inf
#     idx = 0
#     for i in range(1, V+1):
#         if not visited[i] and distance[i] < minV:
#             minV = distance[i]
#             idx = i
#     return idx

inf = 9999999
V, E = map(int, input().split())
start_node = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s].append((e,d))

# visited = [False]*(V+1) 방문처리 필요 없어짐 => 메모리 감소
distance = [inf]*(V+1)

dijkstra(start_node)
for i in range(1, V+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
```