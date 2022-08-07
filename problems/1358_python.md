### 백준 1358번 - 하키

> 2022/08/06 <br>
> 사각형과 원두개로 나누어 그안에 선수의 좌표가 있는지 확인하여 해결했다.

```python
def sq(x, y, w, h, a, b):
    if x <= a <= x+w and y <= b <= y+h :
        return 1
    return 0

def c(x, y, r, a, b):
    if (a-x)**2 + (b-y)**2 <= r**2 :
        return 1
    return 0

w, h, x, y, p = map(int, input().split())
r = h*0.5
ans = 0
for _ in range(p):
    a, b = map(int, input().split())

    j = sq(x, y, w, h, a, b) + c(x, y+r, r, a, b) + c(x+w, y+r, r, a, b)

    if j > 0 :
        ans += 1

print(ans)
```