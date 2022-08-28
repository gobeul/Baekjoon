### 백준 2164번 - 카드2

> 2022/08/28 <br>
> 데크 모듈을 사용하여 큐를 구현하고 풀이했다.

```python
from collections import deque

N = int(input())
Queue = deque()
for i in range(N, 0, -1):
    Queue.append(i)

while len(Queue) != 1:
    a = Queue.pop()
    a = Queue.pop()
    Queue.appendleft(a)

print(Queue[0])
```