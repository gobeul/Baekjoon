### 백준 1629번 - 곱셈

> 2022/09/18 <br>
> 분할 정복 알고리즘, 인터넷을 보며 따라서 구현해봤는데 아직 온전히 이해가 되진 않았다. 우연히 얻어걸려서 맞은 느낌이 강하다.<br>
> 이부분에 대한 추가적인 공부가 필요할듯

```python
def power(a, n, c):
    if n == 0:
        return 1
    
    x = power(a, n//2, c)

    if n % 2 == 0:
        return (x * x) % c
    
    else:
        return (x * x * a) % c

a, b, c = map(int, input().split())
print(power(a, b, c))
```