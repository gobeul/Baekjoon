### 백준 2747번 - 피보나치 수

> 2022/07/16 <br>
> 처음 접근은 단순 재귀함수로 접근해 보았으나 시간초과로 틀렸다. <br>
> 시간을 줄일 수 있는 방법을 고민하다가 최근에 BFS 공부중에 [deque](https://github.com/gobeul/TIL/tree/master/algorithm/deque.md) 라는 자료구조를 접하게 되었고 이를 이 문제에 적용해 보았다.


```python
from collections import deque
n = int(input())
if n == 0:
    print(0)
else:
    p_list = deque([0, 1])
    cnt = 1
    while cnt < n :
        a = p_list.popleft()
        b = a + p_list[0]
        p_list.append(b)
        cnt += 1
    print(p_list[-1])
    print(p_list)
```
