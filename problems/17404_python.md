### 백준 17404번 - RGB거리2

> 2022/11/01 <br>
> 전형적인(?) DP 문제이다.<br>
> 인터넷에서 아이디어를 얻어 해결했다. DP문제 유형에 많이 취약한 거 같다.<br>
> 첫번째 집의 색을 정한 뒤 그 뒷집을 최소값을 쫒도록 결정해 주면서 해결한다.<br>


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    a, b, c = map(int, input().split())
    cost.append((a, b, c))

ans = 999999
for st in range(3): # 1번 집에서 무슨색 칠할지
    dp = [[999999,999999,999999] for _ in range(N)]
    dp[0][st] = cost[0][st] # 색칠
    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    for ed in range(3): # 마지막 색
        if st != ed:
            ans = min(ans, dp[i][ed])

print(ans)
```