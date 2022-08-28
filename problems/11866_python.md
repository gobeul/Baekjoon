### 백준 11866번 - 요세푸스 문제 0

> 2022/08/28 <br>
> 큐를 이용해 볼 수 있는 문제, 원형큐를 구현하여 풀어보았다.

```python
def encQ(item):
    global rear
    rear = (rear+1)%(N+1)
    cQueue[rear] = item

def deQ():
    global front
    front = (front+1)%(N+1)
    return cQueue[front]

N, K = map(int, input().split())
cQueue = [0] * (N+1)
front, rear = 0, 0

for i in range(1, N+1):
    encQ(i)

print("<", end="")
cnt = 0
while front != rear-1:
    cnt += 1
    a = deQ()

    if cnt == K:
        print(str(a)+",", end=" ")
        cnt = 0
    else:
        encQ(a)

print(deQ(), end="")
print(">")
```