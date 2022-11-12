### 백준 2294번 - 동전 2

> 2022/11/12 <br>
> DP 를 이용한 풀이 <br>
> x 원을 만들 수 있는 가장 작은 코인 개수는 (x - y)원을 만들 수 있는 코안 개수 + 1 중에 가장 작은 개수이다.<br>
> 여기서 y는 주어진 코인 가치들


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline


n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))

# x가치의 동전을 만들 수 있는가
possible = [-1]*(k+1)
possible[0] = 0 # 0 원은 동전 0개 필요

for i in range(1, k+1):
    tmp = []
    for j in coins:
        if j <= i and possible[i-j] != -1:
            tmp.append(possible[i-j]+1)

    if tmp:
        possible[i] = min(tmp)

print(possible[k])
```