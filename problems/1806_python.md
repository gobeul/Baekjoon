### 백준 1806번 - 부분합

> 2022/11/15 <br>
> 부분합 문제..? 였던거 같은데 투포인터를 이용해 풀었다..

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def solve():
    if arr[0] == S:
        return 1
    
    i, j = 0, 1
    v = 999999
    k = arr[0] + arr[1]
    while j < N:

        if k < S:
            j += 1
            if j == N:
                break
            k += arr[j]

        else: # 이상
            v = min(v, j-i+1)
            k -= arr[i]
            i += 1
            if i == j:
                k = arr[i]
    
    if v == 999999:
        return 0
    return v


N, S = map(int, input().split())
arr = list(map(int, input().split()))

print(solve())
```