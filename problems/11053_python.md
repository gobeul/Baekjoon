### 백준 11053번 - 가장 긴 증가하는 부분 수열

> 2022/11/07 <br>
> 확인하는 인덱스를 기준으로 그 이하의 값을들 확인해서 보다 작은 원소들중 증가 수열(memo)의 길이 값이 나보다 크다면 그값으로 갱신한다.<br>
> 확인이 끝난 후 자기 자신 까지 포함에 +1 증가 시켜준다. 

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

memo = [0] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and memo[i] < memo[j]: # 증가 될 수 있는 여지가 있다면
            memo[i] = memo[j]
    memo[i] += 1 # 자기자신

print(max(memo))
```