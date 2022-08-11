# 인구이동.. 푸는중

## 16234번 77퍼 시간초과
from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

storage = deque() # 좌표를 저장해야겠다 , 같은 값이 있을 수 있으니, // 국경을 탐색하는 데크
delta = [[-1,0], [1,0], [0,-1], [0,1]] # 상 하 좌 우 델타값

day = 0 # 인구 이동 날
completion = True # 인구이동의 완성 여부
while completion :

    completion = False # 인구이동이 완성되었다고 가정
    day += 1 # 이동 날짜 추가

    check = [] # 이미 방문한 나라의 좌표를 저장
    for i in range(N):
        for j in range(N):
            allied = [] # 연합국을 담을 리스트 (초기화)
            if [i,j] in check : # 좌표값이 방문한 값이면
                pass
            else: # 좌표값이 방문한게 아니면
                check.append([i, j]) # 없으면 등록
                storage.append([i, j])
                allied.append([i, j]) # 연합국 리스트에도 등록
            
            # storage 값을 보고 연합국 연결하기
            while len(storage) != 0 : # storage 가 비어있으면 종료
                dd = 0 # 델타 인덱스 (초기화)
                st = storage.popleft() # 앞에서 빼서 확인
                st_v = arr[st[0]][st[1]] # 기준값 지정
    
                while dd != 4: # 상하좌우 다 검사하면 종료
                    st_ii = st.copy() # st_ii 는 이동해 볼 좌표 ( 초기화 )
                    st_ii[0] += delta[dd][0]
                    st_ii[1] += delta[dd][1] # 인덱스를 이동 시켜보고

                    # 이동해본 인덱스가 범위 안이고 check 리스트에도 없다면
                    if 0 <= st_ii[0] < N and 0 <= st_ii[1] < N : #and (st_ii not in check) : 시간 감소를 위해 밑으로 이동
                        v = abs(st_v - arr[st_ii[0]][st_ii[1]]) # 국경 열 수 있는 값인지??
                        if L <= v <= R and (st_ii not in check) : #국경을 열 수 있다면
                            storage.append(st_ii) # storage 에 추가
                            check.append(st_ii) # check 에도 추가
                            allied.append(st_ii) # 연합국 리스트에도 등록
                    
                    dd += 1 # 델타 좌표 변경

            # 연합국 연결이 끝나고 난 후
            allied_len = len(allied) # 연합국 숫자
            if 2 <= allied_len : # 연합국 숫자가 2이상이여야 분배함
                completion = True # 연합국이 2이상인 경우가 있다면 인구 완성이 된게 아님
                total_population = 0 # 전체 인구수
                for pos in allied: # 연합국 총 인구수 구하기
                    total_population += arr[pos[0]][pos[1]]
                eq_population = total_population // allied_len # 분배될 인구수(소수점 버림)
                for pos in allied:
                    arr[pos[0]][pos[1]] = eq_population # 인구 분배
                
print(day-1) # 이동이 필요없는 날도 더해지기 때문에 -1 해줌