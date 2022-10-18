### 백준 17136번 - 색종이

> 2022/10/18 <br>
> 부르트 포스와 백트래킹 접근으로 가능한 모든 경우의 수를 확인한것 같다.<br>
> 3328 ms 가 나왔고 백준의 다른 분들은 빠르면 200ms 대의 속도를 보였다<br>
> 백트래킹의 조건에서 무엇인가 더 좋은 접근이 있거나 내가 푼 풀이에서 배열들 불필요하게 한번 더 돌거나 하는 경우가 있는거 같다.<br>
> 추후 스터디를 통해 확인해볼 예정!

```python
import sys
sys.stdin = open('ee.txt', 'r')

def find_one():
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                return i, j

    return -1. -1

def CD_paper(si, sj, n, x): # 색종이 붙이기 or 떼기, 시작좌표(i, j), 색종이 크기(n), x == 0 이면 종이 붙이기 / x == 1 이면 종이 떼기
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            arr[i][j] = x


def check(si, sj, n): # 시작좌표(i, j)에서 크기 n인 색종이를 붙일 수 있는가?
    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if not ( 0 <= i < 10 and 0 <= j < 10) or not arr[i][j]:
                return False # 안됨
    return True # 됨

def recure(cnt, n): # cnt = 남은 구역 수, n = 색종이 개수
    global ans, flag

    # if flag:
    #     return

    if n >= ans:
        return

    if not cnt: # 구역을 다 덮었을 경우
        flag = True # 큰 종이 부터 붙이기 때문에 처음 나온 답이 가장 작은 수 일것이다.(가정) -> 안됨
        ans = n
        return

    si, sj = find_one() # 시작 좌표 찾기
    if (si, sj) == (-1, -1): # 남아 있는 구역이 없으면
        ans = min(ans, n)
    
    for i in range(5, 0, -1): # 5 ~ 1번 색종이 붙여보기
        if color_paper[i] and check(si, sj, i): # 남아있는 색종이가 있어야 붙일 수 있음. and n 크기가 딱 맞는지
            # 딱 맞다면
            color_paper[i] -= 1 # i 크기한 개 사용
            CD_paper(si, sj, i, 0) # 붙이기

            recure(cnt-(i**2), n+1) # 재귀, cnt 는 색종이 면적 만큼 빼줌

            color_paper[i] += 1 
            CD_paper(si, sj, i, 1) # 복구

            
        

arr = [list(map(int, input().split())) for _ in range(10)]

cnt = 0 # 구역 개수
for i in range(10):
    for j in range(10):
        if arr[i][j] == 1:
            cnt += 1 

color_paper = [0,5,5,5,5,5] # 사용가능한 색종이 개수

flag = False
ans = 999999

recure(cnt, 0)

if flag:
    print(ans)
else:
    print(-1)
```