# 7569번 토마토
import sys
input = sys.stdin.readline

import copy

def is_correct(pos, N, M, H): # 위치좌표를 받아 [i, j, h] 인덱스 범위 내인지 확인하는 함수
    if 0 <= pos[0] < N : 
        if 0 <= pos[1] < M :
            if 0 <= pos[2] < H :
                return True
    return False


def is_zero(arr): # 2차원 배열안에 0 이있는지 확인하는 함수
    for i in arr:
        if 0 in i:
            return True
    return False

            
M, N, H = map(int, input().split()) # 가로 세로 높이

arr = [ list(map(int, input().split())) for _ in range(N*H) ]
delta = [ [-1,0,0], [1,0,0], [0,-1,0], [0,1,0], [0,0,1], [0,0,-1] ] # 상, 하, 좌, 위, 윗층, 아래층

check_original = [ [True] *M for _ in range(N*H) ]

if is_zero(arr) : # 시작전에 모든 과일이 익어 있으면 끝
    pass
else:
    print(0)
    quit()


# 1 : 익은거 // 0 : 안익은거 // -1 : 빈상자
# 가상 3차원 좌표 [i, j, h]
## 실제 좌표 [i+N*h, j] // 층이 변하면 "행" 만 늘어난다..
day = 0
change = True # 익은 걸로 바꾼 과일이 있을까??
while change : 
    change = False # 바꿀 수 있는 과일이 없다고 가정
    day += 1 # 하루 추가
    check = copy.deepcopy(check_original) # 확인한 과일인지 체크 (초기화)
    for h in range(H): # 층수 0층, 1층, 2층..
        for i in range(N):
            for j in range(M):
                # if arr[i+N*h][j] == 1 and [i, j, h] not in check: # 안익은거면 (True로 해도 되나?) + 확인 안해본거면
                if arr[i+N*h][j] == 1 and check[i+N*h][j] :
                    # check.append([i, j, h]) # 일단 좌표 추가하고
                    check[i+N*h][j] = False

                    # 상하좌우 위아래 탐색
                    dd = 0 # 델타 인덱스
                    st_i = [i, j, h] # 기준 좌표 설정하고
                    while dd != 6:
                        st_ii = st_i.copy() # 기준좌표 초기화
                        st_ii[0] += delta[dd][0] # 일단 이동해 보기
                        st_ii[1] += delta[dd][1]
                        st_ii[2] += delta[dd][2]
                        if is_correct(st_ii, N, M, H): # 인덱스 범위 내 이면.
                            if arr[st_ii[0]+N*st_ii[2]][st_ii[1]] == 0 : # 실제 좌표 확인해서 안익은거(0)인지??
                                arr[st_ii[0]+N*st_ii[2]][st_ii[1]] = 1 # 익은걸로 바꾸기
                                # check.append(st_ii) # check에 추가
                                check[st_ii[0]+N*st_ii[2]][st_ii[1]] = False
                                change = True # 바꿀 수 있는 과일이 있었네

                        dd += 1 # 방향전환

    if is_zero(arr) :
        pass
    else: # 다 익었다면
        change = True
        break

if change : # change 가 True 로 종료됬다 == 시간이 지나 토마토가 다 익었다.
    print(day-1)
else: # change 가 False 로 종료됬다 == 사각지대에 있는 안익은 과일이 있다.
    print(-1)
