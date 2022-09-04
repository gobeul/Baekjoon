### 백준 1966번 - 프린터 큐

> 2022/09/04 <br>
> 리스트 요소를 문서 중요도와 목표문서의 여부(1 or 0)를 가지는 튜플로 만들어 접근했다.

```python
from collections import deque

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())

    doc = deque(list(map(int, input().split())))
    for i in range(N):
        if i != M:
            doc[i] = (doc[i], 0) # 중요도와 문서구분
        else:
            doc[i] = (doc[i], 1)

    cnt = 0
    while 1:
        imp, num = doc.popleft()
        for x, y in doc:
            if imp < x :
                doc.append((imp, num))
                break
        else:
            cnt += 1
            if num == 1:
                print(cnt)
                break
```