### 백준 1967번 - 트리의 지름

> 2022/09/24 <br>
> 트리의 지름을 구하는 방법<br>
> 무작위 노드에서 가장 먼 노드를 구한다. 그 노드를 A하고 하면<br>
> A에서 가장 먼 노드의 길이를 구하면 그 길이가 트리의 지름이 된다.

```python
def BFS(node):
    visited = [False]*(V+1) # 양방향 그래프로 만들어 줬기 때문에 방문처리가 필요하다.
    max_node, max_len = 0, 0
    stack = [(node, 0)]
    visited[node] = True
    while stack:
        now, dis = stack.pop()
        if max_len < dis:
            max_node, max_len = now, dis
        for next, next_dis in graph[now]:
            if not visited[next]:
                visited[next] = True
                stack.append((next, next_dis + dis))
    
    return max_node, max_len


V = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(V-1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d)) # 원래 트리는 단방향 그래프 이지만
    graph[c].append((p, d)) # 거꾸로 올라가야 될 경우가 무조건 있기 때문에 양방향으로 만들어 준다.

tmp_node, dis = BFS(1) # 무작위 노드(1)에서 가장 먼 거리에 있는 노드 tmp_node
x, ans = BFS(tmp_node) # tmp_node 에서 가장 먼 거리에 있는 노드 x와 그떄의 거리 == 트리의 지름(ans)

print(ans)
```