### 백준 10773번 - 제로

> 2022/08/31 <br>
> 스택 문제인가 했는데 실행 시간이 너무 길게 나왔다.

```python
stack = []

k = int(input())
for _ in range(k):
    a = int(input())
    if a != 0:
        stack.append(a)
    else:
        b = stack.pop()

print(sum(stack))
```