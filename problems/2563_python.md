### 백준 22563번 - 색종이

> 2022/07/22 <br>


```python
w_sq = [[False for i in range(100)] for j in range(100)]

n = int(input())
for t in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        w_sq[99-b-i][a-1:a+9] = [True for j in range(10)]

ans = 0
for i in range(100):
    ans += w_sq[i].count(True)

print(ans)
```