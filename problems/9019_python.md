### 백준 9019번 - DSLR

> 2022/09/12 <br>
> pypy3로만 시간초과를 피할 수 있었다.(4888ms) python3 로도 통과해보고 싶은데 방법을 잘 모르겠다..! (푸신분들 다 비공개..)

```python
from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    c = n*2
    if c >= 10000:
        c = c % 10000
    return c

def S(n):
    c = n-1
    if c < 0 :
        c = 9999
    return c

def L(n):
    c = (n*10+n//1000)%10000
    return c

def R(n):
    c = (n+(n%10)*10000)//10
    return c

def BFS():
    while que:
        v, s = que.popleft()

        for k in range(4):
            if k == 0 :
                i = D(v)
                if visited[i] == False:
                    w = s + "D"
                    if i == ep:
                        return w
                    visited[i] = True
                    que.append((i, w))
            elif k == 1 :
                i = S(v)
                if visited[i] == False:
                    w = s + "S"
                    if i == ep:
                        return w
                    visited[i] = True
                    que.append((i, w))
            elif k == 2 :
                i = L(v)
                if visited[i] == False:
                    w = s + "L"
                    if i == ep:
                        return w
                    visited[i] = True
                    que.append((i, w))
            else :
                i = R(v)
                if visited[i] == False:
                    w = s + "R"
                    if i == ep:
                        return w
                    visited[i] = True
                    que.append((i, w))

tc = int(input())
for _ in range(tc):
    visited = [False] * 10000
    st, ep = map(int, input().split())
    que = deque([(st, "")])
    visited[st] = True

    print(BFS())
```