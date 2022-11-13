### 백준 21758번 - 꿀 따기

> 2022/11/13 <br>
> 누적합 문제 <br>
> 꿀과 벌통의 위치 관계를 크게 3가지 경우로 나우어 계산했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 누적 합 만들기
acSum = [0]*n
acSum[0] = arr[0]
for i in range(1, n):
    acSum[i] = acSum[i-1] + arr[i]


# case 1 벌통 - 벌 - 벌
bee1 = acSum[n-1] - arr[n-1] # - bee2 벌 2의 위치값을 하나 빼줘야함

totalMax = 0
for i in range(1, n-1):
    tmp = acSum[i] - arr[i] + bee1 - arr[i]
    totalMax = max(totalMax, tmp)

# case 2 벌 - 벌 - 벌통
bee1 = acSum[n-1] - arr[0] # - bee2 벌 2의 위치값을 하나 빼줘야함

for i in range(1, n-1):
    tmp = acSum[n-1] - acSum[i] + bee1 - arr[i]
    totalMax = max(totalMax, tmp)

# case 3 벌 - 벌통 - 벌
for i in range(1, n-1): # 이경우는 벌통이 움직임
    bee1 = acSum[i] - arr[0]
    bee2 = acSum[n-1] - acSum[i] + arr[i] - arr[n-1]
    totalMax = max(totalMax, bee1+bee2)

print(totalMax)
```