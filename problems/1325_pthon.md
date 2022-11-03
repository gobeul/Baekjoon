### 백준 1325번 - 효율적인 해킹

> 2022/11/03 <br>
> DSF 방식으로 풀어봤는데 python3 시간초과 // pypy3 통과 이다.


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def recur(x):
    visited = [False]*(N+1)
    v = 1
    visited[x] = True

    stack = [x]
    while stack:
        c = stack.pop()
        for i in graph[c]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                v += 1
    
    ans.append(v)
        

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []

for i in range(1, N+1):
    recur(i)

max_v = max(ans)
for i in range(N):
    if max_v == ans[i]:
        print(i+1, end=" ")
print()
```