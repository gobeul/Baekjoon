### 백준 16234번 - 인구이동

> 2022/08/14 <br>
> 7569번과 마찬가지로 구현까지는 무난하게 할 수 있었는데 시간을 줄이는데에서 막혔었다.<br>
> 방문확인을 좌표로 check 리스트에 넣어놨는데 이 방법말고 이차원 배열로 만들고 값은 Trus, False 로 확인할 수 있도록 해서 시간을 많이 줄일 수 있었다.

```python
import sys
input = sys.stdin.readline

def population_moving(N, L, R, arr):

    storage = [] # 좌표를 저장
    delta = [[-1,0], [1,0], [0,-1], [0,1]] # 상 하 좌 우 델타값

    day = 0 # 인구 이동 날
    completion = True # 인구이동의 완성 여부
    while completion :
        completion = False # 인구이동이 완성되었다고 가정
        day += 1 # 이동 날짜 추가
        check = [[False]*N for _ in range(N)] # 방문여부 확인

        for i in range(N):
            for j in range(N):
                allied = [] # 연합국을 담을 리스트 (초기화)
                if check[i][j] : # 좌표값이 방문한 값이면
                    pass
                else: # 좌표값이 방문한게 아니면
                    check[i][j] = True # 없으면 등록
                    storage.append((i, j))
                    allied.append((i, j)) # 연합국 리스트에도 등록
                    allied_len = 0 # 연합국 숫자 초기화
                    total_population = 0 # 연합국 숫자 초기화
                # storage 값을 보고 연합국 연결하기
                while storage : # storage 가 비어있으면 종료
                    (si, sj) = storage.pop() # 빼서 확인
                    st_v = arr[si][sj] # 기준값 지정
                    allied_len += 1 
                    total_population += st_v # 연합국 전체 인구수에 추가
                    for (di, dj) in delta:
                        mi = si + di # 이동해보기
                        mj = sj + dj

                        # 이동해본 인덱스가 범위 안이고 check 리스트에도 없다면
                        if 0 <= mi < N and 0 <= mj < N : #and (st_ii not in check) : 시간 감소를 위해 밑으로 이동
                            v = abs(st_v - arr[mi][mj]) # 국경 열 수 있는 값인지??
                            if L <= v <= R and (check[mi][mj] == False) : #국경을 열 수 있다면 연합국이다.
                                storage.append((mi,mj)) # storage 에 추가
                                check[mi][mj] = True # check 에도 추가
                                allied.append((mi,mj)) # 연합국 리스트에도 등록


                # 연합국 연결이 끝나고 난 후
                if 2 <= allied_len : # 연합국 숫자가 2이상이여야 분배함
                    completion = True # 연합국이 2이상인 경우가 있다면 인구 완성이 된게 아님
                    eq_population = total_population // allied_len # 분배될 인구수(소수점 버림)
                    for (ai,aj) in allied:
                        arr[ai][aj] = eq_population # 인구 분배
                
    return day-1 # 이동이 필요없는 날도 더해지기 때문에 -1 해줌


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(population_moving(N, L, R, arr))
```