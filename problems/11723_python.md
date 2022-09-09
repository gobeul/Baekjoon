### 백준 11723번 - 집합

> 2022/09/08 <br>
> locals()[함수명]() 을 이용하여 input(스트링)으로 받은 함수명으로 함수를 호출할 수 있었다.

```python
import sys
# sys.stdin = open('eee.txt', 'r')
input = sys.stdin.readline

def add(n):
    S[int(n[0])] = 1

def remove(n):
    S[int(n[0])] = 0

def check(n):
    if S[int(n[0])] == 1:
        print(1)
        return
    print(0)
    return

def toggle(n):
    if S[int(n[0])] == 1:
        S[int(n[0])] = 0
    else:
        S[int(n[0])] = 1

def all(n):
    for i in range(21):
        S[i] = 1

def empty(n):
    for i in range(21):
        S[i] = 0


S = [0]*21
K = int(input())

for _ in range(K):
    com, *n = input().split()
    locals()[com](n)
```