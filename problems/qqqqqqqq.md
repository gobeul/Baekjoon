```python
board = [[False for i in range(1001)] for j in range(1001)]
n = int(input())
for k in range(1, n+1):
    a, b, x, y = map(int, input().split())

    for i in range(a, x+a):
        board[i][b:y+b] = [k]*y

for k in range(1, n+1):
    ans = 0
    for i in board:
        ans += i.count(k)
    print(ans)
```

통과 코드   
--------------
불통과 코드

```python
board = [[False for i in range(1001)] for j in range(1001)]
n = int(input())
for k in range(1, n+1):
    a, b, x, y = map(int, input().split())

    for i in range(a, x+a):
        board[i][b:y+b] = [k]*y

for k in range(1, n+1):
    ans = 0
    for i in board:
        for j in i:
            if j == k:
                ans += 1
    print(ans)
```

count, for 둘다 시간복잡도(n) 이 아닌가??