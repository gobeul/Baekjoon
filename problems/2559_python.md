### 백준 2529번 - 수열

> 2022/07/26 <br>
> 시간줄이기 문제 <br>
> N 번째 리스트의 합은 N-1 번째의 리스트 a[s:e] 에서 a[s]를 빼고 a[e]를 더한것과 같다.
> 데크를 이용하여 문제를 '0부터 N 번째 까지의 숫자합이 가장 큰 N을 구하는 문제' 로 바꿔서 풀었다.


```python
import sys
input = sys.stdin.readline

#### 데크를 사용하여 누적 숫자합 문제에 사용할 리스트 뽑기 #######

from collections import deque

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

pointer_list = deque(num_list[:k])
init_sum = sum(pointer_list)
del num_list[:k]

num_list = deque(num_list)

accumulate_list = [0]

while num_list:
    l_v = num_list.popleft()
    wast = pointer_list.popleft()

    pointer_list.append(l_v)

    d = l_v - wast
    
    accumulate_list.append(d)

############################################################
############누적 숫자합이 가장 큰 지점 찾기 ##################

point_1 = 0

accumulate_value = 0 
ans = 0
while point_1 != n-k :
    point_1 += 1
    accumulate_value += accumulate_list[point_1]
    if accumulate_value > ans :
        ans = accumulate_value

print(init_sum + ans)
```



    