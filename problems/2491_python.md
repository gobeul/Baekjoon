### 백준 2491번 - 수열

> 2022/07/23 <br>
> 풀이에 있어 시간을 줄이는 것이 목표인 문제 같다.<br>
> 수열을 검증하면서 수열의 연속(?) 이 끊긴경우에는 해당부분을 리스트에서 삭제하는 방법으로 해결했다.

```python
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
r_num = num.copy()

ans = 2
cnt = 0
while len(num) > ans:
    if num[cnt] <= num[cnt+1] :
        cnt += 1
        if cnt + 1 > ans :
            ans = cnt + 1
    else:
        del num[:cnt+1]
        cnt = 0 

cnt = 0
while len(r_num) > ans:
    if r_num[cnt] >= r_num[cnt+1] :
        cnt += 1
        if cnt + 1 > ans :
            ans = cnt + 1
    else:
        del r_num[:cnt+1]
        cnt = 0

if n == 1:
    ans = 1
    
print(ans)
```