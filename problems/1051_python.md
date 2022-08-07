### 백준 1051번 - 숫자 정사각형

> 2022/08/06 <br>
> 반복문으로 최대크기의 정사각형부터 최소 크기까지 찾아가며 풀었다.

```python
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())

a = min(N, M)

k = True
while k:
    for i in range(N-a+1):
        for j in range(M-a+1):
            if board[i][j] == board[i][j+a-1] == board[i+a-1][j] == board[i+a-1][j+a-1]:
                print(a*a)
                k = False
                break
        if k == False:
            break
    a -= 1
```
