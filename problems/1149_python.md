### 백준 1149번 - RGB거리

> 2022/08/15 <br>
> 동적프로그래밍(Dynamic programming)

```python
n = int(input())

house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

# dp[i][0] = i번째까지 i번째 집을 R(0)로 칠했을때 최솟값
dp = [[0]*3 for _ in range(n)]

dp[0][0] = house[0][0] # 0 = R
dp[0][1] = house[0][1] # 1 = G
dp[0][2] = house[0][2] # 2 = B

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1]+house[i][0], dp[i-1][2]+house[i][0])
    dp[i][1] = min(dp[i-1][0]+house[i][1], dp[i-1][2]+house[i][1])
    dp[i][2] = min(dp[i-1][0]+house[i][2], dp[i-1][1]+house[i][2])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
```