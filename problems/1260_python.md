### 백준 1260번 - DFS와 BFS

> 2022/09/11 <br>
> 방문가능한 노드가 여러개 있을때 무조건 작은 수 부터 방문해야 한다.

```python
from collections import deque

N, M, sp = map(int, input().split())

lines = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

for i in lines:
    i = i.sort(reverse=True)

# DFS
stack = [sp]
visited = [False] * (N+1)
# visited[sp] = True
dfs = []
while stack :
    num = stack.pop()
    if visited[num] == False:
        dfs.append(num)
        visited[num] = True
        for i in lines[num]:
                stack.append(i)

for i in lines:
    i = i.sort()

#BFS
que = deque([sp])
visited = [False] * (N+1)
visited[sp] = True
bfs = []
while que :
    num = que.popleft()
    bfs.append(num)
    for i in lines[num]:
        if visited[i] == False:
            visited[i] = True
            que.append(i)

print(*dfs)
print(*bfs)
```