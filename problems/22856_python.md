### 백준 22856번 - 트리순회

> 2022/11/16 <br>
> 중위순회의 마지막 노드.. 이부분이 이해가 잘 안간다<br>
> 왜 1 - 2 로 이루어진 트리의 중위순회 마지막 노드가 2가아닌 1이 되는 걸까

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve():
    cnt = N-1
    now = 1
    move = 0
    while cnt > 0:
        if node[now][0] != -1 and not visited[node[now][0]]:
            visited[node[now][0]] = True
            cnt -= 1
            now = node[now][0]
            move += 1
            continue

        elif node[now][1] != -1 and not visited[node[now][1]]:
            visited[node[now][1]] = True
            cnt -= 1
            now = node[now][1]
            move += 1
            continue

        else: # 부모노드로 이동
            now = tree[now]
            move += 1
    
    while now != last_node:
        now = tree[now]
        move += 1

    return move


last_node = 0
def traverse(n):
    global last_node
    if n == -1:
        return
    traverse(node[n][0])
    last_node = n
    traverse(node[n][1])


N = int(input())
node = [[] for _ in range(N+1)]
tree = [0]*(N+1) # 부모 노드 
visited = [False]*(N+1)
visited[1] = True
for _ in range(N):
    n, r, l = map(int, input().split())
    node[n].append(r)
    node[n].append(l)
    if r != -1:
        tree[r] = n
    if l != -1:
        tree[l] = n


last_node = 0
traverse(1)


print(solve())

```