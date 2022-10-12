### 백준 16918번 - 봄버맨

> 2022/10/12 <br>
> 매초마다 배열을 돌며 계산을 해줬기에 시간소요가 상당했다.(제한시간이 2초라서 통과는 했다.)<br>
> 다른 분들의 풀이를 보니 일정 주기를 가지고 배열의 모양이 반복되는 것을 이용하여 시간을 많이 줄인 듯하다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def time_go(): # 시간 감소
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                visited[i][j] -= 1

def set_boom():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
                visited[i][j] = 3

def boom():
    stack = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 'O':
                stack.append((i,j))
                arr[i][j] = '.'

    while stack:
        i, j = stack.pop()
        for di, dj in delta:
            mi, mj = i+di, j+dj
            if 0 <= mi < N and 0 <= mj < M :
                arr[mi][mj] = '.'
                visited[mi][mj] = 0

def answer():
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end="")
        print()

delta = [(1,0), (-1,0), (0,1), (0,-1)]

N, M, T = map(int, input().split())

arr = [ list(input()) for _ in range(N) ]

visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'O': # 폭탄 설치
            visited[i][j] = 3

T -= 1 # 처음 1초
time_go()
flag = True
while T:
    T -= 1
    time_go()
    if flag: # 폭탄 설치할 차례 
        set_boom()
        flag = False
    else:
        boom()
        flag = True

answer()
```