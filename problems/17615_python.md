### 백준 17615번 - 볼 모으기

> 2022/12/25 <br>

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
balls = list(input().rstrip())

# 0. 각 색상의 공 카운트
red, blue = 0, 0
for i in balls:
    if i == 'R':
        red += 1
    else:
        blue += 1

ans = N
# 1. 파란색을 모두 오른쪽으로 모을 경우
# 맨 오른쪽에 연속된 파란색을 제외하고 남은 파란색 개수를 카운트 한다.
tmp = blue
for i in range(N-1, -1, -1):
    if balls[i] == 'R':
        break
    else:
        tmp -= 1
ans = min(ans, tmp)

# 2. 빨간색을 오른쪽으로 모을경우
tmp = red
for i in range(N-1, -1, -1):
    if balls[i] == 'B':
        break
    else:
        tmp -= 1
ans = min(ans, tmp)

# 3. 파란색을 왼쪽으로 모을경우
tmp = blue
for i in range(N):
    if balls[i] == 'R':
        break
    else:
        tmp -= 1
ans = min(ans, tmp)

# 4. 빨간색을 왼쪽으로 모을경우
tmp = red
for i in range(N):
    if balls[i] == 'B':
        break
    else:
        tmp -= 1
ans = min(ans, tmp)

print(ans)
```