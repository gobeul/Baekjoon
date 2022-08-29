### 백준 10866번 - 덱

> 2022/08/29 <br>
> 데크 구현문제이다 양사이드에서 어떻게 넣을 수 있을까 고민하다가 stack 크기를 엄청 크게 잡고 중간 인덱스 부터 시작하는 방법을 사용했다..<br>
> 통과는 됐지만 문제의도는 이런 방법이 아닐꺼란 생각이 든다.

```python
import sys
input = sys.stdin.readline

def Push_f(n):
    global front, rear
    if rear == front:
        Push_b(n)
        return
    front -= 1
    stack[front] = n

def Push_b(n):
    global rear
    stack[rear] = n
    rear += 1

def Pop_f():
    global rear, front
    if rear == front:
        print(-1)
        return
    print(stack[front])
    front += 1

def Pop_b():
    global rear, front
    if rear == front:
        print(-1)
        return
    rear -= 1
    print(stack[rear])

def Size():
    print(rear-front)

def Empty():
    global rear, front
    if rear == front:
        print(1)
    else:
        print(0)

def Front():
    global front, rear
    if rear == front:
        print(-1)
    else:
        print(stack[front])

def Back():
    global front, rear
    if rear == front:
        print(-1)
    else:
        print(stack[rear-1])

stack = [0]*100000
rear, front = 50000, 50000


N = int(input())
for _ in range(N):
    com = list(input().split())
    if com[0] == "push_back":
        Push_b(com[1])
    elif com[0] == "push_front":
        Push_f(com[1])
    elif com[0] == "pop_back":
        Pop_b()
    elif com[0] == "pop_front":
        Pop_f()
    elif com[0] == "size":
        Size()
    elif com[0] == "empty":
        Empty()
    elif com[0] == "front":
        Front()
    else:
        Back()
```