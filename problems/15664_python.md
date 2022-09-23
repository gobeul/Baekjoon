### 백준 15664번 - N과 M (10)

> 2022/09/23 <br>
> 조합과 순열시리즈 열번째
> 주어진 원소안에서 중복 부분가능??, 수열내의 순서는 오름차순 + 전체 출력은 사전순으로 + 주어진 원소 중에서 중복된 원소가 있을 수 있으며 중복된 만큼 원소를 사용할 수 있으나 수열 자체는 중복되면 안됨.
  
```python
def recur(s, last):
    if s == M:
        print(*arr)
        return

    for i in range(last, N):
        if cnt_nums[i] > 0:
            arr[s] = set_nums[i]
            cnt_nums[i] -= 1
            recur(s+1, i)
            cnt_nums[i] += 1

N, M = map(int, input().split())
nums = list(map(int, input().split()))

set_nums = sorted(list(set(nums)))
cnt_nums = [0]*len(set_nums)
for i in nums:
    idx = set_nums.index(i)
    cnt_nums[idx] += 1

N = len(set_nums)
arr = [0]*M

recur(0, 0)
```