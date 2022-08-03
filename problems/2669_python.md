### 백준 2669번 - 직사각형 네개의 합집합의 면적 구하기

> 2022/08/02 <br>
> 2차원 배열로 좌표평면을 만들고 주어진 좌표점을 이용해 면적부분을 1로 칠하여 면적계산을 했다. 

```python
board = [[False for i in range(101)] for j in range(101)]

for _ in range(4):
    a, b, x, y = map(int, input().split())

    for i in range(y, b, -1): # 면적만큼 1로 채우기
        for j in range(x, a, -1):
            board[i][j] = 1

ans = 0
for i in board:
    ans += sum(i)

print(ans)
```