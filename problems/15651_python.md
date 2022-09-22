### 백준 15651번 - N과 M (3)

> 2022/09/22 <br>
> 조합과 순열시리즈 세번째
> N개에서 M 개 뽑기, 중복허용 + 순서 상관있게

```python
def recur(step):
    if step == M:
        print(*arr)
        return
    for i in range(1, N+1): # 중복이 허용됨으로 제한이 조건이 없다 싶이 한다.
        arr[step] = i
        recur(step+1)

N, M = map(int, input().split())
arr = [0 for _ in range(M)]

recur(0)
```