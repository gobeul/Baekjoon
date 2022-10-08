### 백준 11055번 - 가장 큰 증가 부분 수열

> 2022/10/08 <br>
> 실버2 난이도라서 어렵진 않았는데 다른 유형의 실버2 보단 어려웠다.<br>
> dp 유형의 문제인것을 파악하기 까지, 어떻게 dp를 구현할 것 인지 고려하는 부분까지 ..<br>
> 아직 dp문제가 약한것 같다.

```python
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0]*N

for i in range(N):
    dp[i] = arr[i]
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
```