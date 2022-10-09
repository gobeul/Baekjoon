### 백준 6603번 - 로또

> 2022/10/09 <br>
> 조합문제. N과M 시리즈를 풀었다보니 쉽게 풀 수 있었다.

```python
import sys
input = sys.stdin.readline

def recur(s, last):
    if s == 6:
        print(*lotto)
        return

    for i in range(last+1, n):
        lotto[s] = arr[i]
        recur(s+1, i)

while 1:
    n, *arr = map(int, input().split())

    if n == 0:
        break

    arr.sort()
    lotto = [0]*6
    recur(0, -1)

    print()
```