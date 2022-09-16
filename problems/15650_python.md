### 백준 15650번 - N과 M(2)

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