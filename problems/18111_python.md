### 백준 18111번 - 마인크래프트

> 2022/09/08 <br>
> python3 로는 시간초과로 통과하지 못한 코드 이다. pypy3로만 통과한 코드.

```python
import sys
sys.stdin = open('eee.txt', 'r')
input = sys.stdin.readline


N, M, B = map(int, input().split())

arr = []
for i in range(N):
    arr += list(map(int, input().split()))
    # arr += k

min_block = min(arr) 
# 최적의 최대 높이 == (전체 총합 + B ) // N*M
max_block = (sum(arr) + B) // (N*M)

ans = 500*500*256
ans_H = 0
for i in range(min_block, max_block+1): # i 높이 로 만들때 걸리는 시간
    timE = 0
    for j in arr:
        kk = i-j
        if kk > 0: # j에 블럭을 더해줘야 되는 경우 시간 +1
            timE += kk
        elif kk < 0: # 블럭 제거 과정 시간 +2
            timE += -2*(kk)


    if ans >= timE:
        ans = timE
        ans_H = i

print(ans, ans_H)
```