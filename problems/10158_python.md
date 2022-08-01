### 백준 10158번 - 개미

> 2022/08/01 <br>
> 이동한 거리(시간)가 전체 너비의 2배면 제자리라는 점을 이용하여 계산했다.

```python
W, H = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

a = (x+t) % W
b = (y+t) % H


if ((x+t)//W)%2 :
    a = W - a

if ((y+t)//H)%2 :
    b = H - b

print(a, b)
```