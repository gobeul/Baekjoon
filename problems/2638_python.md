### 백준 2638번 - 또 다른 치즈 문제

> 2022/09/27 <br>
> 또다른 치즈 문제, 2636과 비슷한 문제였다.<br>
> 
> 다시금 알게 된 점이 있다면 BFS 의 방문처리는 큐에 append 될때 처리를 해줘야지만 쓸데없는 메모리 낭비를 막을 수 있다.<br>
> -> 예시로 pop 할때 방문처리를 해준다면 이전에 다른 좌표값에서 중복으로 죄표들이 append될 수 있다. (방문 처리가 안되었기 때문)

```python
import sys
input = sys.stdin.readline

def check(si, sj): # 2면 이상이 공기인가?
    cnt = 0
    for di, dj in delta:
        i, j = si + di, sj + dj
        # 가장 자리는 치즈가 없으므로 인덱스 검사는 필요 없다.
        if visited[i][j] and not arr[i][j]: # 바깓 공기만 True이다.
            cnt += 1
    
    if cnt >= 2:
        return True
    return False

def solve():
    global ans
    flag = True
    cheese = []

    while flag:
        ans += 1
        flag = False

        while stack:
            si, sj = stack.pop()
            for di, dj in delta:
                i, j = si+di, sj+dj
                if 0 <= i < N and 0 <= j < M and not visited[i][j]:
                    if not arr[i][j]: # 빈공간
                        visited[i][j] = True
                        stack.append((i, j))
                    elif arr[i][j]: # 치즈
                        visited[i][j] = True
                        cheese.append((i,j))

        # 겉면 에 치즈 다 찾았다면.
        tmp = [] # 녹지 않는 치즈들
        while cheese: # 녹이기
            flag = True # 녹일 치즈가 하나라도 있다면
            si, sj = cheese.pop()
            if check(si, sj): # 녹을 수 있는 치즈 인가?
                stack.append((si, sj))
            else:
                tmp.append((si, sj))

        for i, j in stack:
            visited[i][j] = True
            arr[i][j] = 0

        cheese = tmp

    ans -= 1
    

delta = [(1,0),(-1,0), (0,1),(0,-1)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
stack = [(0,0), (0,M-1), (N-1,0), (N-1, M-1)] # 가장자리는 치즈가 없다.
for i, j in stack:
    visited[i][j] = True 

ans = 0
solve()
print(ans)
```