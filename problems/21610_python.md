### 백준 21610번 - 마법사 상어와 비바라기

> 2022/10/15 <br>
> 크게 어렵지 않은 구현 문제였는데 비내리고 물복사 하는 부분을 동시에 진행해서 해맸다.
> 중간중간 디버깅으로 배열등을 출력해서 문제점을 찾을 수 있었다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def move(d, s): # 구름이동
    di, dj = delta[d][0]*s, delta[d][1]*s
    for idx, (i, j) in enumerate(cloud):
        # N 으로 나눈 나머지 = 인덱스 범위 넘어가도 이어지게
        cloud[idx] = ((i+di)%N, (j+dj)%N)

    visit_cloud(cloud) # 구름 이동 후 방문처리


def make_cloud(): # 새로운 구름 생성
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                new_cloud.append((i, j))
    not_visit_cloud(cloud)
    return new_cloud


def rainny(): # 비내리고 물복사 ( 비 먼저 내리고  -> 다시 배열 순회로 물 복사 ) -> 비 내리기 + 물복사 동시하면 안됨
    # 왜냐면 물복사 할때 0칸에 구름이 있으면 물복사 칸에 추가할 수 있는데 동시에 진행되면 반영 안 될 수 있음
    for i, j in cloud:
        arr[i][j] += 1

    for i, j in cloud:
        water = 0
        for di, dj in delta2:
            mi, mj = i+di, j+dj
            if 0 <= mi < N and 0 <= mj < N and arr[mi][mj]:
                water += 1
        arr[i][j] += water


def not_visit_cloud(before): # 구름 방문처리 해제
    for i, j in before:
        visited[i][j] = False

def visit_cloud(cloud): # 구름 방문처리
    for i, j in cloud:
        visited[i][j] = True


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = [tuple(map(int, input().split())) for _ in range(K)]

delta = [-1, (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)] # 델타
delta2 = [(-1,-1), (-1,1), (1,1), (1,-1)] # 대각 델타
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 시작 구름위치
visited = [[False]*N for _ in range(N)] # 구름 방문처리

for d, s in command:
    move(d, s)
    rainny()
    cloud = make_cloud()


ans = 0
for i in range(N):
    for j in range(N):
        ans += arr[i][j]

print(ans)
```