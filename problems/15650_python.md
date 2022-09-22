### 백준 15650번 - N과 M(2)

> 2022/09/22 <br>
> 조합과 순열시리즈 두번째
> N개에서 M 개 뽑기, 중복없이 + 순서 상관없이

```python
def recur(step, start): # 순서 및 중복을 컨트롤 해줄 start
    if step == M:
        print(*arr)
        return
    for i in range(start, N+1):
        arr[step] = i
        recur(step+1, i+1) # i +1 => 방금 바꿔준거보다 하나 크게

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

recur(0, 1)
```


> 2022/09/16 <br>
> 모듈을 사용한 조합 풀이

```python
from itertools import combinations

N, M = map(int, input().split())
arr = [ i for i in range(1, N+1)]

ans = list(combinations(arr, M))

for i in ans:
    print(*i)
```