### 백준 15666번 - N과 M (12)

> 2022/09/23 <br>
> 조합과 순열시리즈 열두번째(마지막?)
> 주어진 원소안에서 중복사용가능, 수열내의 순서 오름차순 + 전체 출력은 사전순으로 + 주어진 원소 중에서 중복된 원소가 있을 수 있으며 있음 하지만 수열 자체는 중복되면 안됨.
  
```python
def recur(s, last):
    if s == M:
        print(*arr)
        return 

    for i in range(last, N):
        arr[s] = set_nums[i]
        recur(s+1, i)

N, M = map(int, input().split())
nums = list(map(int, input().split()))

set_nums = sorted(list(set(nums)))
N = len(set_nums)

arr = [0]*M

recur(0, 0)
```