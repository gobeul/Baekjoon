### 백준 15665번 - N과 M (11)

> 2022/09/23 <br>
> 조합과 순열시리즈 열한번째
> 주어진 원소안에서 중복가능, 수열내의 순서 구분 + 전체 출력은 사전순으로 + 주어진 원소 중에서 중복된 원소가 있을 수 있으며 있음 하지만 수열 자체는 중복되면 안됨.
  
```python
def recur(s):
    if s == M:
        print(*arr)
        return
    
    for i in range(N):
        arr[s] = set_nums[i]
        recur(s+1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))

set_nums = list(set(nums)) # set 으로 중복만 제거하고 M개를 중복을 어용하여 뽑기
set_nums.sort()

N = len(set_nums)
arr = [0]*M

recur(0)
```