### 백준 1202번 - 보석도둑

> 2022/10/14 <br>
> 최대힙을 사용하여 시간을 줄여하는 문제였다.<br>
> 가방은 용량이 작은거 부터 확인해서 그 가방에 들어갈 수 있는 보석들을 최대 힙에 넣어 준다. (보석도 무게 기준으로 정렬한다.)<br>
> 보석이 계속 무거워 지다가 더이상 가방에 들어갈 수 없는 보석이나오면 <br>
> 지금까지 최대힙에 들어간 보석들중 가장 가치가 높은 보석을 꺼낸다. -> 이과정에서 최대 힙이기 때문에 heappop 한번이면 연산이 끝난다.<br>
> 이를 계속 반복하면 힙에는 결국 기준가방에 들어갈 수 있는 보석들만 존재 함으로 heappop으로 가장 가치 있는 보석만 꺼낼 수 있다. -> 그리디
> 힙으로 우선 순위 큐를 사용하면 큐에 원소가 들어갈때마다 정렬을 할 필요가 없어서 시간을 효율적으로 줄일수 있는 것 같다.

```python
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jem = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jem.sort(reverse=True) # pop() 연산을 사용할거라서 무게기준 내림차순으로 정렬해주기.
bag.sort()

hp, ans = [], 0
for b in bag:
    # 가방에 넣을 수 있는 잼들 최대힙에 추가
    while jem:
        w, v = jem.pop()
        if w > b:
            jem.append((w,v)) # 다시 넣어주기
            break
        heapq.heappush(hp, -v)
    
    if hp: # 힙에 보석이 있을때만
        ans += heapq.heappop(hp) # 최대값 빼서 가방에 넣기

print(-ans)
```