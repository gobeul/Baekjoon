### 백준 21318번 - 피아노 체조

> 2022/10/20 <br>
> 누적합문제.. N 이 최대 10만개, Q 가 최대 10만개 였기때문에 누적합 리스트를 만드는 과정에서도 하나의 if문 + 1개의 조건으로 끝내야 했던것 같다.<br>
> if 문 2개를 적용하니 실제로는 시간초과가 나왔다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
diff = list(map(int, input().split()))
Q = int(input())

arr = [0]*N
for i in range(1, N):
    if diff[i-1] > diff[i]:
        arr[i] += arr[i-1] + 1
    else:
        arr[i] += arr[i-1]

for _ in range(Q):
    s, e = map(int, input().split())
    print(arr[e-1] - arr[s-1])
```