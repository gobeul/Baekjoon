### 백준 22869번 - 징검다리 건너지 (small)

> 2022/12/10 <br>
> N-1에서 0으로 도착하는 BFS를 구현했다면 더 빠르게 갈 수 있었을까?


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def move(i, j):
    v = (j-i)*(1 + abs(arr[i] - arr[j]))
    if v <= K:
        return True # K보다 작은 힘이면 이동 가능
    return False


N, K = map(int, input().split())
arr = list(map(int, input().split()))

possible = [False]*N
possible[0] = True

for j in range(1, N):
    for i in range(j-1, -1, -1):
        # j 로 갈수 있는 i 번째 돌이 존재 하는가?
        # 먼저 i 로 갈 수 있고 i -> j 힘이 충분하면 건널 수 있다.
        if possible[i] and move(i,j):
            possible[j] = True
            break # j 로 갈 수 있는게 확인 되면 더 볼 필요는 없음

if possible[N-1]: # 마지막 돌로 판별
    print('YES')
else:
    print('NO')
```