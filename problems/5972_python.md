### 백준 5972번 - 택배 배송

> 2022/10/24 <br>
> 간단한 다익스트라 구현문제였다.<br>
> 그런데 실행시간이 생각보다 커서 인터넷에서 비슷한 코드를 찾아 돌려봤는데 시간이 10배 차이가 나드라..<br>
> 아직 두 코드 간에 유의미한 차이를 잘 모르겠다.<br>

> 찾았다.. input 을 intput 으로 써서 sys사용을 전혀 못하고 있었다...

```python
import sys
intput = sys.stdin.readline
import heapq
"""
다익스트라
"""
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))
    graph[e].append((d, s))

inf = 1e9
dis = [inf]*(N+1)
dis[1] = 0

def djikstra():

    hq = [(0, 1)] # 비용/노드번호
    while hq:
        cost, node = heapq.heappop(hq)

        if dis[node] < cost:
            continue
        for add_cost, next_node in graph[node]:
            tmp_cost = cost + add_cost
            if dis[next_node] > tmp_cost:
                dis[next_node] = tmp_cost
                heapq.heappush(hq, (tmp_cost, next_node))

    return dis[N]         


print(djikstra())
```


### 비슷한 코드 같지만 시간면에서 10배 정도 빠른 코드
```python
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9) 

N, M = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[N]

print(dijkstra(1))
```