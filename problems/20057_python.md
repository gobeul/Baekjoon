### 백준 20057번 - 마법사 상어와 토네이도

> 2022/10/21 <br>
> 회전하는 분배 좌표를 i,j 로 적절하게 사용하여 좌표를 나타낼 수 있었다.

> 알파를 단순하게 55% 생각했는데 그게 아니였다. '나머지' 라고 명시해준 이유가 있었다. 소수점을 버리기 때문에 알파에는 정말 나머지를 배분해줘야했다.

> 마찬가지로 밖으로 나간 먼지양을 계산하면 안됐다. 이역시 소수점을 버리기 때문!<br>
> 남아 있는 먼자의 양으로 밖으로 나간 먼지의 양을 구했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

"""
왼쪽 x칸 -> 아래 x칸 -> 오른쪽 x+1칸 -> 위쪽 x+1칸 -> 왼쪽 x+2칸 ...
"""

####

def is_range(i, j): # 인덱스 범위 내인지
    if 0 <= i < N and 0 <= j < N :
        return True
    return False

# [a, 5, 10, 10, 7, 7, 2, 2, 1, 1]
def dust_move(i, j, pi, pj, v): # 방향 좌표 i, j // 현재 위치 좌표 pi, pj // v == 먼지양
    global ans

    D = [
        (i*2, j*2), # 5%
        (i+j, i+j), (i-j, j-i), # 10%
        (j,i), (-j,-i), # 7%
        (2*j, 2*i), (-2*j, -2*i), # 2%
        (j-i, i-j), (-j-i, -i-j), # 1%
        (i, j), # 알파
    ]
    bye = 0 # 나눠진 먼지 양
    for d in range(10):
        ti, tj = D[d][0]+pi, D[d][1]+pj
        tv = int(dust[d]*v)
        bye += tv
        if is_range(ti, tj):
            arr[ti][tj] += tv # 먼지 분배

    if is_range(ti, tj):
        arr[ti][tj] += v - bye # 알파를 마지막에 배분... 소수점 버림 때문에..

    arr[pi][pj] = 0 # 흩날린 먼지

def sum_dust():
    v = 0
    for i in range(N):
        for j in range(N):
            v += arr[i][j]
    
    return v
    

delta = [(-1,0), (1,0), (0,-1), (0,1)] # 상 하 좌 우
dust = [0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01, 0]  # 알파 = 55% 로 보면 안됨..

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total_dust = sum_dust() # 처음 모래양

si, sj = N//2, N//2 #시작점

ans = 0 # 격자 밖으로 나간 먼지
ending = False
for k in range(1, 500): # k는 그 방향으로 이동하는 칸 수
    if k%2: # 왼쪽 아래는 홀 수 칸 이동
        for s in range(1, k+1):
            sj -= 1
            dust_move(0, -1, si, sj, arr[si][sj]) # 왼쪽이동
            if (si, sj) == (0, 0) :
                ending = True
                break

        if ending:
            break
        
        for s in range(1, k+1):
            si += 1
            dust_move(1, 0, si, sj, arr[si][sj]) # 아래 이동
            if (si, sj) == (0, 0) :
                ending = True
                break


    else: # # 오른쪽 위는 짝 수 칸 이동
        for s in range(1, k+1):
            sj += 1
            dust_move(0, 1, si, sj, arr[si][sj]) # 오른쪽 이동
            if (si, sj) == (0, 0) :
                ending = True
                break
        
        if ending:
            break
        
        for s in range(1, k+1):
            si -= 1
            dust_move(-1, 0, si, sj, arr[si][sj]) # 위쪽 이동
            if (si, sj) == (0, 0) :
                ending = True
                break

    if ending:
        break

M = sum_dust()
print(total_dust - M) # 나간 모래 == 처음 모래 - 남아있는 모래
```