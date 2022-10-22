### 백준 19598번 - 최소 회의실 개수

> 2022/10/22 <br>
> 회의시간을 시작-끝 시간으로 정렬하고 우선순위큐를 이용하여 끝 시간이 빠른 것 부터 비교할 수 있었다.<br>
> 


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

from collections import deque
import heapq

N = int(input())

time_table = []
for _ in range(N):
    s, e = map(int, input().split())
    time_table.append((s,e))

time_table.sort()
time_table = deque(time_table)

s, e = time_table.popleft()

room = [e]
ans = 1 # 회의실 개수

while time_table:
    s, e = time_table.popleft()
    time = heapq.heappop(room)
    if s < time: # 시작 시간이 회의실 사용중인 가장 빠른 끝시간 부터 비교한다.
        heapq.heappush(room, time)
        heapq.heappush(room, e)
        ans += 1
    else:
        heapq.heappush(room, e)

print(ans)
```