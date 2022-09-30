### 백준 13549번 - 숨바꼭질 3

> 2022/09/30 <br>
> BFS 로 풀이 했는데 순간이동 가중치가 0 이기 때문에 appendleft() 를 사용하여 고려해줄 수 있었다.<br>
> 가중치가 0,1 두개뿐이여서 가능한 방법이었고, 가중치 값의 종류가 3 이상이라면 다익스트라를 사용해야 가능한 풀이일 것이다.


```python
import sys
from collections import deque

def BFS(s):
    que = deque([(s, 0)])
    visited[s] = True

    while que:
        pos, cnt = que.popleft()
        if pos == K:
            return cnt
        # 순간이동 = appendleft
        j = pos*2
        if 0 <= j <= 100000 and not visited[j]:
            visited[j] = True
            que.appendleft((j, cnt))
        # 걷기 = append
        w = pos+1
        if 0 <= w <= 100000 and not visited[w]:
            visited[w] = True
            que.append((w, cnt+1))
        w = pos-1
        if 0 <= w <= 100000 and not visited[w]:
            visited[w] = True
            que.append((w, cnt+1))


N, K = map(int, input().split())
visited = [False]*(100001)

print(BFS(N))
```