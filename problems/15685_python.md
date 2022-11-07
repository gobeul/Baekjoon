### 백준 15685번 - 드래곤 커브

> 2022/11/02 <br>
> 지나온 방향(델타인덱스)을 기준으로 거꾸로 90도 씩 회전하여 추가해 준다면 드래곤 커브를 그릴 수 있다.<br>

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def draw(lst, si, sj):
    arr[si][sj] = True
    for d in lst:
        si += delta[d][0]
        sj += delta[d][1]
        arr[si][sj] = True

def find_squar(i, j):
    global ans
    for si in range(i, i+2):
        for sj in range(j, j+2):
            if not arr[si][sj]:
                return
    ans += 1

arr = [[False]*101 for _ in range(101)] # 100 x 100 좌표
# delta = [(0,1), (1,0), (0,-1), (-1,0)] # 오 아 왼 위
delta = [(0,1), (-1,0), (0,-1), (1,0)] # 오 위 왼 아
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    genetation = [d] # 0세대
    cnt = 0
    while cnt < g:

        for i in range(len(genetation)-1, -1, -1): # 지나온 길을 거꾸로 탐색하여
            k = (genetation[i] + 1)%4  # 델타 회전
            genetation.append(k)
        
        cnt += 1

    # 세대 생성이 끝났으면 그리기
    draw(genetation, y, x)

# 모든 드래곤커브를 그리고 난 후 사각형 찾기
ans = 0
for i in range(100):  # 101 이 아닌 100 으로 줌으로써 인덱스 범위 내에 있게 한다.
    for j in range(100):
        find_squar(i, j)

print(ans)

```