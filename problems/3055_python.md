### 백준 3055번 - 탈출

> 2022/08/19 <br>
> 물이 퍼지는 작업과 고슴도치의 이동이 같이 이루어 지는 작업이지만 물이 퍼지는 것을 먼저 수행하여 작업량을 줄였다???

```python
# 세로, 가로
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)] # 맵.
delta = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우 델타 값

water = [] # 물 위치
stone = [] # 돌
go = [] # 이동할 스택

water_visit = [[False]*C for _ in range(R)] # 방문기록(물)
go_visit = [[False]*C for _ in range(R)] # 방문기록(고슴도치)
for i in range(R): # 초기값 설정
    for j in range(C):
        if arr[i][j] == "*":
            water.append((i,j))
            water_visit[i][j] = True
        elif arr[i][j] == "X":
            stone.append((i,j))
        elif arr[i][j] == "S":
            go.append((i,j))
            go_visit[i][j] = True
        elif arr[i][j] == "D":
            end = (i,j) # 도착지점

tmp_water = []
tmp_go = [] # 임시 스택
time = 0
ending = True # 동굴 도착하면 False
while ending: # 동굴 도착할때 까지
    time += 1
    while water: # 물 스택이 없을 때까지, 물먼저 진행
        sti, stj = water.pop() # 기준값 지정
        for di, dj in delta:
            mi = sti + di
            mj = stj + dj # 이동해보기
            # 물 : 이동한 위치가 인덱스 범위 내 + 동굴 아님 + 돌 아님
            if 0 <= mi < R and 0 <= mj < C and water_visit[mi][mj] == False and arr[mi][mj] != "D" and arr[mi][mj] != "X":
                water_visit[mi][mj] = True # 물 방문 처리
                tmp_water.append((mi,mj)) # 스택에 추가

    while go: # 고슴도치 진행
        sti, stj = go.pop() 
        for di, dj in delta:
            mi = sti + di
            mj = stj + dj
            # 고슴도치 : 이동한 위치가 인덱스 범위 내 + 돌 아님 + 물방문한곳 아님
            if 0 <= mi < R and 0 <= mj < C and go_visit[mi][mj] == False and water_visit[mi][mj] == False and arr[mi][mj] != "X":
                if arr[mi][mj] == "D" : # 근데 가뵜더니 동굴이었다면
                    ending = False
                    break
                go_visit[mi][mj] = True # 고슴도치 방문 처리
                tmp_go.append((mi,mj)) # 스택에 추가
    
    # 스택 갱신하기
    if tmp_go and ending: # ending 이 True 인채로 넘어와야 갱신 진행
        water = tmp_water[:] # 갱신 
        go = tmp_go[:]
        tmp_water = [] # 초기화
        tmp_go = []
    else: # tmp_go 가 비어있다 == 안전하게 갈 수 있는 곳이 없다.
        break # ending = True 인채로 브레이크

if ending:
    print("KAKTUS")
else:
    print(time)
```