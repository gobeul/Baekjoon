### 백준 1189번 - 컴백홈

> 2022/08/16 <br>
> 탐색 문제였지만 최단거리를 구하는 것이 아니었다.<br>
> 모든 경로에 대해서 방문처리를 다르게 진행해야 했기에 재귀함수에 방문인자값을 넘겨줘서 해결할 수 있었다.

```python
ans = 0 # 총 가지수
def DFS(R, C, K, arr, visited, cnt, i, j): # cnt = 1, i = R-1, j = 0  시작점 좌표값 준것. cnt는 이동 거리
    global ans # ans 를 전역 변수로 설정
    delta = [[-1,0], [1,0], [0,1], [0,-1]] # 북, 남, 동, 서 델타
    if K == cnt and (i, j) == (0, C-1): # 도착점
        ans += 1
        # 따로 리턴 값은 주지 않는다 어짜피 ans 를 전역변수로 설정했기 때문이다.
        return

    for di, dj in delta: # 상하좌우 다 이동해보고
        mi = i + di 
        mj = j + dj
        
        # 인덱스 범위 내이고 , T가 아니고 방문도 안했다면
        if 0 <= mi < R and 0 <= mj < C and arr[mi][mj] != "T" and visited[mi][mj] :
            visited[mi][mj] = False # 방문 처리 해주고
            cnt += 1 # 이동거리 추가해 주고 
            DFS(R, C, K, arr, visited, cnt, mi, mj) # 재귀호출
            #### 이부분을 해줌으로써 모든 경로마다 방문기록 값을 가지게 할 수 있었다.####
            visited[mi][mj] = True  # 방문 처리한거 원상복구
            cnt -= 1 # 이동거리 원상복구
            ##########################################################################

    # for 문 다 돌렸음 끝
    return
            

R, C, K = map(int, input().split()) # 가로 세로 거리

arr = [ list(map(str, input())) for _ in range(R) ]
visited = [[True]*C for _ in range(R)] # 방문 기록
visited[R-1][0] = False # 시작점 방문 표시
DFS(R, C, K, arr, visited, 1, R-1, 0)

print(ans)
```