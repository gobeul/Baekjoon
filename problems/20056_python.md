### 백준 20056번 - 마법사 상어와 파이어볼

> 2022/09/28 <br>
> 구현하는데 재밌었던 문제였다.<br>
> 요즘 종종 2차원 배열에 서 이동후 같은 칸에 있는 것들을 특정하게 처리하는 문제가 많이 보였는데 9/28 기준으로 이방법이 제일 좋은 것 같다.<br>
>
> 초기 방문 값 False -> False 상태로 한개들어오면 필요한 정보들(그 좌표에 들어온 원소의 개수도 같이 카운트 해준다.)의 리스트로 False 값을 바꿔줌 + 해당 좌표를 다른 리스트(tmp)에 저장<br>
> 이동이 필요한 stack이 비워지면 tmp를 for 문 돌리면서 visited 값을 확인하고 해당값이 2개 이상 이면 필요한 계산 수행.

```python
import sys
input = sys.stdin.readline

delta = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] # 0 ~ 7

N, M, K = map(int, input().split()) # 격자크기, 파이어볼 개수, 이동명령

stack = []
for _ in range(M):
    i, j, m, s, d = map(int, input().split()) # 좌표, 질량, 속력, 방향
    stack.append((i-1,j-1,m,s,d))

visited = [[False]*N for _ in range(N)]

move = 0
while move != K:
    move += 1
    tmp = [] # 이동 후 위치한 좌표정보

    while stack:
        i, j, m, s, d = stack.pop()

        # 이동
        i = (i+delta[d][0]*s)%N
        j = (j+delta[d][1]*s)%N

        if not visited[i][j]:
            tmp.append((i,j))
            visited[i][j] = [1, m, s, d%2, d] # 개수, 질량, 속도, 뱡항(홀짝), 1개 있을때 방향
        else:
            visited[i][j][0] += 1
            visited[i][j][1] += m
            visited[i][j][2] += s
            visited[i][j][3] += d%2

    # 이동이 끝난 후
    ans = 0 # 전체 질량 갱신
    for i, j in tmp:
        # 2개 이상 파이어볼이 위치했다면 / 합쳐진 질량이 5보다 크다면
        if visited[i][j][0] > 1 and visited[i][j][1]//5 > 0 :
            # 방향이 모두 짝수 or 홀수 인 경우
            if visited[i][j][3] == 0 or visited[i][j][3] == visited[i][j][0]:
                for d in range(0, 8, 2):
                    stack.append((i, j, visited[i][j][1]//5, visited[i][j][2]//visited[i][j][0], d))
            else:
                for d in range(1, 8, 2):
                    stack.append((i, j, visited[i][j][1]//5, visited[i][j][2]//visited[i][j][0], d))
            ans += (visited[i][j][1]//5) * 4 # 4개로 쪼개짐

        elif visited[i][j][0] == 1:
            stack.append((i, j, visited[i][j][1], visited[i][j][2], visited[i][j][4]))
            ans += visited[i][j][1]

        visited[i][j] = False # 방문기록 초기화

print(ans)
```