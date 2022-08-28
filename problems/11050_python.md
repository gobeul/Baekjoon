### 백준 11050번 - 이항 계수 1

> 2022/08/28 <br>

```python
"""
이항계수 N!/K!(N-K)!
"""
def fact(n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    
    return n * fact(n-1)

N, K = map(int, input().split())
ans = fact(N) // (fact(K) * fact(N-K))

print(ans)
```