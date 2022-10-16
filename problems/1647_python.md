### 백준 1647번 - 도시 분할 계획

> 2022/10/16 <br>
> SMT 를 구해서 가장 긴 간선의 길이를 뺌으로서 두 마을을 나누는 방식인데...<br>
> SMT 알고리즘인 크루스칼과 프림 모두 시간 초과가 나왔다.<br>
> 그래서 우선순위큐를 이용한 프림 알고리즘이 이란 방법을 보고 제출했다.<br>
> 아직 크루스칼, 프림 알고리즘이 익숙치 않아서 더 연습이 필요하다.

```python
import sys
import heapq
input = sys.stdin.readline

"""
SMT  - 우선순위 큐를 사용한 프림 알고리즘
"""

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

hq, cnt, ans, max_dis = [(0,1)], 0, 0, 0
visited =[False]*(N+1)

while cnt != N:
    dis, node = heapq.heappop(hq)
    if not visited[node]:
        cnt += 1
        visited[node] = True
        ans += dis
        max_dis =  max(max_dis, dis)
        for next, next_dis in graph[node]:
            if not visited[next]:
                heapq.heappush(hq, (next_dis, next))

print(ans - max_dis)
```