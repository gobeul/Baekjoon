### 백준 5557번 - 1학년

> 2022/11/19 <br>
> DP 문제... 역시 생각하는게 쉽지가 않다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
DP = [[0]*21 for _ in range(N)]
DP[0][arr[0]] = 1 # 첫번째 숫자 

for i in range(1, N-1):
    for j in range(21):
        if not DP[i-1][j]: # 1 이상이어야 j를 만들 수 있는게 있다는 뜻
            continue
        plus = j + arr[i]
        minus = j - arr[i]
        if plus <= 20: # 더해서 20 이하
            DP[i][plus] += DP[i-1][j] # DP[i-1][j] 번은 만들 수있는 경우의 수가 있다.
        if 0 <= minus: # 빼서 0 이상
            DP[i][minus] += DP[i-1][j]

print(DP[N-2][arr[-1]]) # 마지막 값을 만들 수 있는 경우의 수 출력
```