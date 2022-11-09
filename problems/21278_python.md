### 백준 21278번 - 호석이 두 마리 치킨

> 2022/11/09 <br>
> 이중 for문으로 두 치킨집의 모든 경우의 수 마다 최소의 왕복거를 계산해 풀었다.<br>
> 모든 경우 수를 계산헸고 별다은 가지치기를 하지 않아서 인지 python3 로는 시간초과가 발생했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque

def BFS(node, lst): # BFS로 최단 거리 계산
    visited = [False]*(N+1)
    que = deque([(node, 0)]) # node 번호와 거리
    visited[node] = True
    while que:
        v, d = que.popleft()
        for next in graph[v]:
            if not visited[next]:
                if next in lst:
                    return d+1
                visited[next] = True
                que.append((next, d+1))
    

    
def calculate(lst):
    global ans

    val = 0
    for node in range(1, N+1):
        if val >= ans[0]:
            return
        if node in lst: # 그 도시에 치킨집이 있는 경우
            continue

        val += BFS(node, lst)

    if val >= ans[0]:
        return 
    
    ans = (val, lst)


N, M = map(int, input().split()) 

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e) # 양방향
    graph[e].append(s)

ans = (9999999999, []) # 왕복 방향이라 x2 해줄거임
for first in range(1, N):
    for second in range(2, N+1):
        calculate([first, second])        
    
print(*ans[1], ans[0]*2)
```