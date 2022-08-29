### 백준 10828번 - 스택

> 2022/08/29 <br>
> 간단한 스택 구현 문제이긴한데 `sys` 사용안하면 시간초과.. 사용하면 80ms..<br>
> 이렇게나 차이가 나다니..

```python
import sys
input = sys.stdin.readline

def Push(n):
    global top
    top += 1
    stack[top] = n

def Pop():
    global top
    if top == -1:
        print(-1)
        return
    print(stack[top])
    top -= 1

def Size():
    print(top+1)

def Empty():
    global top
    if top == -1:
        print(1)
    else:
        print(0)

def Top():
    global top
    if top == -1:
        print(-1)
    else:
        print(stack[top])

stack = [0]*100000
top = -1

N = int(input())
for _ in range(N):
    com = list(input().split())

    if com[0] == "push":
        Push(com[1])
    elif com[0] == "pop":
        Pop()
    elif com[0] == "size":
        Size()
    elif com[0] == "empty":
        Empty()
    else:
        Top()
```