### 백준 2461번 - 대표 선수

> 2023/01/10 <br>
> 힙큐를 이용해서 매번 가장 작은 값을 빼는 방법으로 풀이했다.

```python
import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(sorted(tmp, reverse=True)) # 내림차순 정렬


ans = 10**10
hq = []
maxValue = -1
for i in range(N):
    k = arr[i].pop() # i 행에서 가장 작은 값 뽑기
    maxValue = max(maxValue, k)
    heapq.heappush(hq, (k, i)) # (값, 몇 번째 행의 값인지)

while 1:
    minValue, team = heapq.heappop(hq)
    ans = min(ans, maxValue-minValue)
    if arr[team]:
        k = arr[team].pop()
        heapq.heappush(hq, (k, team))
        maxValue = max(maxValue, k)
    else:
        break

print(ans)
```