### 백준 20438번 - 출석체크

> 2022/10/06 <br>
> 누적합을 계산해서 적은 시간안에 풀이하는게 목표인 문제 같았는데...<br>
> 처음에 누적합을 생각하지 못하고 부루트포스 식으로 풀어봤는데 통과가 됐다.. 1260ms (누적합 사용시 136ms가 나왔다)<br>
> 아래의 풀이는 누적합 풀이.


```python
import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

students = [1]*(N+3) 
sleep = list(map(int, input().split()))
code = list(map(int, input().split()))


for i in sleep:
    students[i] = -1

for i in code:
    if students[i] < 0:
        continue
    for k in range(i, N+3, i): # i배수 번 출책
        if students[k] < 0:
            continue
        students[k] = 0

for i in sleep:
    students[i] = 1

accumulation = [0]*(N+3) # 누적합
for i in range(3, N+3):
    accumulation[i] = students[i] + accumulation[i-1]

for _ in range(M):
    s, e = map(int, input().split())
    print(accumulation[e] - accumulation[s-1])
```