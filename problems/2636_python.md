### 백준 2636번 - 치즈

> 2022/08/18 <br>
> 빈공간을 전체 탐색하는 방법으로 치즈경계면을 구할 수 있었다.

```python
# 세로, 가로
h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)] # 2차원 판

delta = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하좌우 델타
visited = [[False]*w for _ in range(h)] # 방문기록
visited[0][0], visited[h-1][0], visited[0][w-1], visited[h-1][w-1] = True, True, True, True
stack = [(0,0), (h-1,0), (0,w-1), (h-1, w-1)] # 4개의 꼭지점에서 출발
cheese = [] # 한시간뒤 녹을 치즈
time = 0
while 1:
    while stack: # 스택이 비어있으면 종료
        sti, stj = stack.pop() # 스택에서 하나 뺴서 기준좌표 설정
        for di, dj in delta:
            mi = sti + di # 델타 이동
            mj = stj + dj

            # 인덱스 범위 내이고 미 방문인지 확인
            if 0 <= mi < h and 0 <= mj < w and visited[mi][mj] == False :
                visited[mi][mj] = True # 방문처리
                if arr[mi][mj] == 1: # 치즈 라면
                    cheese.append((mi,mj)) # 녹을 치즈에 추가
                    arr[mi][mj] == 0 # 치즈 녹이기
                else: # 치즈가 아니면
                    stack.append((mi,mj)) # 스택에 추가해서 이동할 수 있도록

    if cheese: # 녹을 치즈가 있다면
        # 스택이 다 비워졌으면 
        time += 1 # 시간 경과
        stack = cheese[:] # 녹은 치즈위치가 출발 위치가 됨
        cheese_cnt = len(cheese) # 치즈 개수 기록
        cheese = [] # 치즈 초기화
    else: # 녹을 치즈가 없다면
        break

print(time)
print(cheese_cnt)
```