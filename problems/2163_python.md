### 백준 2163번 - 초콜릿 자르기

> 2022/07/19 <br>


```python
N, M = map(int, input().split())

if N*M == 1:
    print(0)
elif N == 1:
    print(M-1)
elif M == 1:
    print(N-1)
else:
    print(N*(M-1) + (N-1))
```
