### 백준 2531번 - 회전 초밥

> 2022/10/10 <br>
> pypy로만 시간초과를 벗어 날 수 있는 코드..<br>
> python3 로 통과한 분의 코드를 보니<br>
> 내 코드에서 인덱스 회전을 위해 매번 i %= N 연산을 해준다는점<br>
> add 로 일일히 값을추가한다는 점 이 시간초과의 주된 원인인것 같다.
>
> 슬라이싱으로 배열을 잘라 추가해준다면(물론 넘어가는 부분에 대해서는 다른 조건이 추가되어야 겠지만) python3로도 통과할 수 있을 것이다. 

```python
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))


idx, ans = 0, 0
while idx != N:
    tmp = set()
    for i in range(idx, idx+k):
        i %= N
        tmp.add(arr[i])
        
    tmp.add(c)
    tmp_cnt = len(tmp)

    idx += 1
    if tmp_cnt == k+1:
        print(tmp_cnt)
        break

    ans = max(tmp_cnt, ans)

print(ans)
```