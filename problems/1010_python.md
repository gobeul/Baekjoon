### 백준 1010번 - 다리 놓기

> 2022/07/24 <br>
m 개에서 서로다른 n 개를 뽑는 경우의 수와 같다. (combination)
mCn = m! / (n! * (m-n)!)

```python
from math import factorial

t = int(input())
for i in range(t):
    n, m = map(int, input().split())

    print(int(factorial(m) / (factorial(n) * factorial(m-n))))
```
