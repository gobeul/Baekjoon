### 백준 13549번 - 숨바꼭질 4

> 2022/12/05 <br>
> 경로를 저장해야 되는 문제 조건이 있어서 배열에 경로를 그댈 저장했는데 메모리 초과가 발생했다.<br>
> 메모리 초과를 줄일 수 있는 방법을 고민하다 도움을 얻었는데 딕셔너리에 값을 저장하는 방법을 보았다.<br>
> key = 출발 , value = 도착이 아니라 key = 도착 , value = 출발 으로 한 이유는 마지막에 딕셔너리 정보를 가지고 경로를 뽑아야 되는데 <br> 
> 같은 출발점에 여러 도착점이 될 수 있기 때문이다 (왜냐하면 1, 2, 3에 2가 출발점이면 1도 3도 출발점이 2 이기 때문) <br>
> 그래서 key = 도착 , value = 출발 으로 두면 ket 값이 중복되지 않기 때문에 이렇게 둔것


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque

def solve(s, e):
    if s >= e: # s 가 더 크면 순간이동이 안됨
        print(s - e)
        for i in range(s, e-1, -1):
            print(i, end=" ")
        print()
        return

    pos = [False]*(e+11)
    pos[s] = 0 # 걸린 시간
    path = {} # 경로 저장 딕셔너리 키 = 도착 , 벨류 = 출발
    # 키가 출발이 되게 되면 한개에 출발에 여러가지 도착이 있을 수 있기 때문에 
    # 벨류 값을 유한하게 둘 수가 없음

    que = deque()
    que.append(s)
    while que:
        p = que.popleft()
        t = pos[p]
        if p == e:
            break

        n = p - 1 # 뒤로 이동
        if e+10 >= n >= 0 and (not pos[n] or pos[n] > t + 1) :
            pos[n] = t + 1
            que.append(n)
            path[n] = p
        
        n = p + 1 # 앞으로 이동
        if e+10 >= n >= 0 and (not pos[n] or pos[n] > t + 1) :
            pos[n] = t + 1
            que.append(n)
            path[n] = p
        
        n = p*2 # 순간이동
        if e+10 >= n >= 0 and (not pos[n] or pos[n] > t + 1) :
            pos[n] = t + 1
            que.append(n)
            path[n] = p

    ans = [e]
    while 1:
        n = ans[-1]
        p = path[n]
        ans.append(p)

        if p == s:
            break
    
    n = len(ans) - 1
    print(n)
    for i in range(n, -1, -1):
        print(ans[i], end=" ")
    print()
    return 


s, e = map(int, input().split())
solve(s, e)
```