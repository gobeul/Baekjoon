### 백준 1934번 - 최소공배수

> 2022/07/21 <br>
> 하나하나 찾는 것은 시간초과로 인하여 해결할 수 없었다.<br>
> [유클리드 호제법](https://github.com/gobeul/TIL/tree/master/algorithm/euclidean_algorithm.md)을 이용하여 시간제한안에 실행이 가능했다.

```python
def GCD(a, b):
    if a == b:
        return a
    elif a > b:
        r = a%b
        if r == 0:
            return b
        else:
            return GCD(b, r)
    else:
        r = b%a
        if r == 0:
            return a
        else:
            return GCD(a, r)

def LCM(a, b):
    G = GCD(a, b)
    return (a*b)//G

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(LCM(a, b))
```
