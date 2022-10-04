### 백준 2668번 - 숫자고르기

> 2022/10/03 <br>
> 출반점을 정해서 따라가다가 다기 출발점이 나오면 지금까지의 경로를 저장하는 방법으로 풀이했다.

```python
import sys
input = sys.stdin.readline

def trans(lst):
    global size

    for i in lst:
        size += 1
        ans.append(i)
        visited[i] = True

def recur(lst):
    next = nums[lst[-1]]
    if next == start:
        trans(lst)
        return lst
    if not tmp_visited[next]:
        tmp_visited[next] = True
        recur(lst+[next])
        tmp_visited[next] = False

N = int(input())
nums = [-1]
for _ in range(N):
    nums.append(int(input()))

visited = [False]*(N+1)
tmp_visited = [False]*(N+1) # 1 - 4 - 5 - 4 - 5 .. 같은 케이스를 피하기 위해

size = 0
ans = []

size, ans = 0, []
for i in range(1, N+1):
    if not visited[i]:
        start = i
        recur([i])

print(size)
ans.sort() # 작은 수 부터 출력
for i in ans:
    print(i)
```