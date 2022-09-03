### 백준 1874번 - 스택 수열

> 2022/09/03 <br>
> 문제 조건을 따라 가면서 풀이했다

```python
import sys
input = sys.stdin.readline

n = int(input())
num = [i for i in range(1, n+1)]
p1 = 0 

stack = []

sq = []
p2 = 0
for _ in range(n):
    a = int(input())
    sq.append(a)
ans = []
while p1 != n:
    
    if num[p1] == sq[p2]:
        p1 += 1
        p2 += 1
        ans.append('+')
        ans.append('-')
    elif stack and stack[-1] == sq[p2]:
        k = stack.pop()
        ans.append("-")
        p2 += 1
    else:
        stack.append(num[p1])
        p1 += 1
        ans.append("+")

# 스택에서 빼기
while stack:
    a = stack.pop()
    if a != sq[p2]:
        break
    p2 += 1
    ans.append('-')

if stack:
    print("NO")
else:
    for i in ans:
        print(i)
```