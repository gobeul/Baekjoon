### 백준 2138번 - 전구와 스위치

> 2022/10/31 <br>
> 0 번 스위치만 정해지면 그뒤에 i번 째 스위치는 i-1 번째 스위치의 상태를 보고 온오프를 결정할 수 있다.<br>
> 즉 0번 스위치를 누를때 와 누르지 않을때 2가지 경우를 비교하여 해결할 수 있다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def turn(i):
    if i == 0:
        st[i], st[i+1] = (st[i] + 1)%2, (st[i+1] + 1)%2
    elif i == N-1:
        st[i-1], st[i] = (st[i-1] + 1)%2, (st[i] + 1)%2
    else:
        st[i-1], st[i], st[i+1] = (st[i-1] + 1)%2, (st[i] + 1)%2, (st[i+1] + 1)%2

def check():
    for i in range(N):
        if st[i] != ed[i]:
            return False
    return True

N = int(input())
st = list(map(int, list(input().rstrip())))
ed = list(map(int, list(input().rstrip())))
tmp = st[:]

ans = 999999
# 0 번 스위치를 누를 경우
turn(0)
cnt = 1
for i in range(1, N):
    if st[i-1] != ed[i-1]:
        turn(i)
        cnt += 1
if check():
    ans = min(ans, cnt)

# 0번 스위치를 누르지 않을 경우
st = tmp[:] # 배열 초기화
cnt = 0
for i in range(1, N):
    if st[i-1] != ed[i-1]:
        turn(i)
        cnt += 1
if check():
    ans = min(ans, cnt)

if ans == 999999:
    print(-1)
else:
    print(ans)
```
