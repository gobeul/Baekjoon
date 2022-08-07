### 백준 1004번 - 어린왕자

> 2022/08/05 <br>
> 원방정식을 이용하여 좌표가 원의 내부에 있는지 외부에 있는지 확인하여 풀었다.

```python
def planet(x, y, a, b, r):
    j = (a-x)**2 + (b-y)**2

    if j > r**2: #외부
        return 1
    else: #내부
        return 2

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    n = int(input())
    for i in range(n):
        a, b, r = map(int, input().split())
        if (planet(x1, y1, a, b, r) + planet(x2, y2, a, b, r)) == 3: # 두 점중 하나만 원의 내부에 있어야 행성 경계를 지난다.
            ans += 1
    print(ans)
```