### 백준 10026번 - 적록색약

> 2022/09/12 <br>
> 색약인과 비색약인 두 번 BFS 를 돌려서 해결하였다.

```python
from collections import deque

delta = [(0,1), (0,-1), (1,0), (-1,0)]
N = int(input())
arr = [list(input()) for _ in range(N)]

# 비색약인
ans1 = 0 # 구역 카운트
visited = [[True]*N for _ in range(N)] # True 가 비방문
pic = N*N # 방문 횟수 이게 0 이 되어야 다 방문한거 

order = [] 
que = deque([(0,0)])

while 1:
    ans1 += 1 # 구역하나 추가
    color = arr[que[0][0]][que[0][1]]
    visited[que[0][0]][que[0][1]] = False
    pic -= 1
    while que:
        sti, stj = que.popleft()
        for di, dj in delta:
            mi = sti + di
            mj = stj + dj
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj]:
                if arr[mi][mj] == color:
                    que.append((mi, mj))
                    visited[mi][mj] = False
                    pic -= 1
                else:
                    order.append((mi,mj))

    if pic == 0:
        break
    else:
        while 1:
            oi, oj = order.pop()
            if visited[oi][oj]:
                que.append((oi, oj))
                break


# 색약인
ans2 = 0 # 구역 카운트
visited = [[True]*N for _ in range(N)] # True 가 비방문
pic = N*N # 방문 횟수 이게 0 이 되어야 다 방문한거 

order = [] 
que = deque([(0,0)])

while 1:
    ans2 += 1 # 구역하나 추가
    color = arr[que[0][0]][que[0][1]]
    if color == 'R' or color == 'G':
        color = "RG"
    visited[que[0][0]][que[0][1]] = False
    pic -= 1
    while que:
        sti, stj = que.popleft()
        for di, dj in delta:
            mi = sti + di
            mj = stj + dj
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj]:
                if arr[mi][mj] in color:
                    que.append((mi, mj))
                    visited[mi][mj] = False
                    pic -= 1
                else:
                    order.append((mi,mj))

    if pic == 0:
        break
    else:
        while 1:
            oi, oj = order.pop()
            if visited[oi][oj]:
                que.append((oi, oj))
                break

print(ans1, ans2)
```