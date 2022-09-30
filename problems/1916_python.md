### 백준 1916번 - 최소비용 구하기

> 2022/09/30 <br>
> 가중치가 있는 그래프의 최단 거리 구하는 문제 유형이었다.<br>
> 우선순위 큐를 사용하여 다익스트라 알고리즘을구현해ㅆ다.<br>
> 제한시간이 0.5초로 나와있어서 아마 일반적인 다익스트라는 시간초괴가 나올 것이다.

```python
import sys
sys.stdin = open("eee.txt", "r")
import heapq # 우선순위 큐를 위한 힙큐
input = sys.stdin.readline

def dijkstra(s):
    all_cost[s] = 0
    que = []
    heapq.heappush(que, (0, s))

    while que:
        cost, node = heapq.heappop(que)
        if all_cost[node] < cost:
            continue
        for next, next_cost in graph[node]:
            tmp_cost = cost + next_cost
            if all_cost[next] > tmp_cost:
                all_cost[next] = tmp_cost
                heapq.heappush(que, (tmp_cost, next)) 


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)] # 도시정보
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c)) 

A, B = map(int, input().split())

inf = 99999999999
all_cost = [inf]*(N+1)

dijkstra(A)
print(all_cost[B])
```