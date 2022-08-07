### 백준 1003번 - 피보나치 함수

> 2022/08/05 <br>
> 0번 째부터 0과 1의 출력 횟수를 조금만 적어보면서 규칙을 찾을 수 있었다.

```python
t = int(input())
for i in range(t):
    N = int(input())
    a = 1
    b = 0
    cnt = 0
    while cnt != N :
        a, b = b, a+b
        cnt += 1

    print(a, b)
```