### 백준 16928번 - 뱀과 사다리 게임

> 2022/09/14 <br>
> 처음 문제를 보고 단순하게 그냥 dp로 구현을 생각했다.<br>
> 하지만 시간초과가 나왔다 (아마, 뱀과 사다리가 둘다 0 인 케이스, 뱀과 사다리로 많은 순환이 생기는 경우등이 있어서?)<br>
> 탐색 문제처럼 방문처리를 해줌으로서 문제를 해결할 수 있었다.

```python
a, b = map(int, input().split())

jump = {}
for _ in range(a+b):
    f, r = map(int, input().split())
    jump[f] = r

visited =[True] * 101 
dp = [[] for _ in range(101)]
dp[0].append(1)
visited[1] = False
cnt = 0
while 1:
    cnt += 1
    for now in dp[cnt-1]:
        for dice in range(1, 7):
            moving = now + dice
            try:
                moving = jump[moving]
            except:
                pass
            if moving >= 100:
                print(cnt)
                quit()
            if visited[moving]:
                dp[cnt].append(moving)
                visited[moving] = False

```