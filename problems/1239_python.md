### 백준 1239번 - 차트

> 2022/08/17 <br>
> 순열을 구하는 모듈을 이용하여 모든 순열의 조합을 구한다.<br>
> 원형차트의 시작점 값을 기입하여 시작점 들간의 차가 50 이면 그 쌍은 원점을 지나는 라인이다.

```python
from itertools import permutations

def is_50(arr, n): # 원소 두개의 차가 50이 되는 경우의 수 구하기
    c = 0
    for i in range(n): # 중복은 어짜피 0이라 고려 안해도 됨
        for j in range(n):
            if arr[i] - arr[j] == 50 :
                c += 1
    return  c

n = int(input())

arr = list(map(int, input().split()))

# 배열가능한 모든 경우의 수 구하기 (순열) (모듈 사용)
all = list(permutations(arr, n))


ans = 0
# 순열로 구한 값들로 차트 시작점 만들기
for case in all:
    sp = [0]*n
    for i in range(1, n):
        sp[i] = sp[i-1] + case[i-1]
    # 구한 시작점으로 중심선 개수 구하기
    a = is_50(sp, n)
    if ans < a :
        ans = a

print(ans)
```