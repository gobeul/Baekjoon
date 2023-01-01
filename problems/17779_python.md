### 백준 17779번 - 게리멘더링 2

> 2023/01/01 <br>
> 구현할 기능을 정리해두고 하나씩 구현해가며 해결했다!<br>


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque

'''
0. 전체 인구수 구하기
1. 4개의 꼭지점 특정하고 배열안에 다 들어가 있는지 확인 => 다 들어 가야 선거구 5개 나옴
2-1. 4개의 꼭지점 연결하여 방문처리 
2-2. 4개의 꼭지점 동서남북을 기준으로 북의 위쪽은 1번/ 남의 밑은 4번 / 동의 오른쪽은 2번 / 서의 왼쪽은 3번으로 하고 방문처리
3-1. 배열의 꼭지점에서 출발하여 BFS 돌려서 각 선거구 인구수 뽑기
3-2. 남은 인구 5번 선거부에 할당
7. 계산 후 비교
'''
def isRange(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False

def fun1(i, j, d1, d2): # 1번
    vertex = [(i,j), (i+d1,j+d1), (i+d1+d2,j+d1-d2), (i+d2,j-d2)] # 북, 동, 남, 서 꼭지점
    for i, j in vertex:
        if not isRange(i,j):
            return False # 선거구 나눌 수 없는 경우
    return vertex # 나눌 수 있는 경우

def fun2(lst):
    d, ni, nj = 0, lst[0][0], lst[0][1]
    while d != 4: # 테두리 그리기(2-1)
        visited[ni][nj] = True
        if d == 0: # 북에서 동으로 가는 중..
            ni += 1
            nj += 1
        elif d == 1: # 동에서 남으로 가는 중..
            ni += 1
            nj -= 1
        elif d == 2:
            ni -= 1
            nj -= 1
        else:
            ni -= 1
            nj += 1
        
        if (ni, nj) in lst:
            d += 1
    
    for idx, (si, sj) in enumerate(lst): # 2-2 그리기
        while 1:
            si += delta[idx][0]
            sj += delta[idx][1]
            if isRange(si, sj):
                visited[si][sj] = True
                population[idx] += arr[si][sj]
            else:
                break


def fun3(n): # 3-1번 / n : 선거구 번호
    i, j = election_start[n]
    que = deque([(i,j)])
    visited[i][j] = True

    while que:
        i, j = que.popleft()
        population[n] += arr[i][j]
        for di, dj in delta:
            mi, mj = i+di, j+dj
            if isRange(mi, mj) and not visited[mi][mj]:
                visited[mi][mj] = True
                que.append((mi,mj))

    
    population[4] -= population[n]


    
delta = [(-1,0), (0,1), (1,0), (0,-1)] # 북 동 남 서
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0번
tp = 0 # 총 인구수
for i in arr:
    tp += sum(i)

election_start = [(0,0), (0,N-1), (N-1, N-1), (N-1,0)] # 4개의 선거구 출발점 (북 동 남 서)

ans = 9999999999
for i in range(1,N):
    for j in range(1,N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                lst = fun1(i, j, d1, d2)
                if lst: # 나눌 수 있으면
                    visited = [[False]*N for _ in range(N)] # 방문배열 초기화
                    population = [0,0,0,0,tp] # 각 선거구 인구 수
                    fun2(lst)
                    for n in range(4):
                        fun3(n)
                    
                    tmp = max(population) - min(population)
                    if tmp == 9:
                        print(i, j, d1, d2)

                    ans = min(ans, tmp)

print(ans)
```