### 백준 7569번 - 토마토

> 2022/08/12 <br>
> 시간초과가 나서 정말 여러번 수정을 거듭한 문제이다.
> bfs, dfs 에 대해서 조금은 이해할 수 있었던 문제였다.

```python
# 7569번 토마토
import sys
input = sys.stdin.readline

def is_correct(h, y, x, N, M, H): # 위치좌표를 받아 [h, i, j] 인덱스 범위 내인지 확인하는 함수
    if 0 <= y < N : 
        if 0 <= x < M :
            if 0 <= h < H :
                return True
    return False

def tomato(M, N, H, arr): ## 풀이 함수
    delta = [ [0,-1,0], [0,1,0], [-1,0,0], [1,0,0], [0,0,1], [0,0,-1] ] # 상, 하, 좌, 위, 윗층, 아래층
    
    today = [] 

    day = 0
    zero = 0 # 처음 안익은 사과 개수
    ## 사전작업 - 익어 있는 사과 찾기
    for h in range(H): # 층수 0층, 1층, 2층..
            for i in range(N):
                for j in range(M):
                    if arr[h][i][j] == 1: # 익은거 찾기
                        today.append((h, i, j)) # 리스트에 추가 (튜플)
                    elif arr[h][i][j] == 0:
                        zero += 1

    if zero == 0: # 처음에 안익은 사과가 없다면
        return 0

    while today : # today 가 비어 있지 않다면 계속 반복
        day += 1
        next_time = []

        for (sh, sy, sx) in today: # today.pop() 보다

            for (dx, dy, dh) in delta: # 델타인덱스로 접근하는 방법보다 
                th = sh + dh # 일단 이동해보기
                ty = sy + dy
                tx = sx + dx
                if is_correct(th, ty, tx, N, M, H): # 인덱스 범위 내 이면.
                    if arr[th][ty][tx] == 0 : # 실제 좌표값 확인해서 안익은거 인지 확인하고
                        arr[th][ty][tx] = 1  # 익은걸로 바꾸고
                        zero -= 1
                        next_time.append((th, ty, tx)) # 리스트에 튜플 형식으로 추가 

                        if zero == 0:
                            return day

        today = next_time
    return -1


M, N, H = map(int, input().split()) # 가로 세로 높이
arr = [ [list(map(int, input().split())) for _ in range(N)] for __ in range(H) ] # 3차원 배열? 처럼 만들기

print(tomato(M,N,H,arr))
```