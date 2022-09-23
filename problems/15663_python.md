### 백준 15663번 - N과 M (9)

> 2022/09/23 <br>
> 조합과 순열시리즈 아홉번째
> 주어진 원소안에서 중복 부분가능??, 수열내의 순서 구분 + 전체 출력은 사전순으로 + 주어진 원소 중에서 중복된 원소가 있을 수 있으며 중복된 만큼 원소를 사용할 수 있으나 수열 자체는 중복되면 안됨.
  
```python
def recur(s):
    if s == M:
        print(*arr)
        return

    for i in range(N):
        if cnt_nums[i] > 0: # visit 가 아니라 있는 만큼 사용 9가 2번 등장하면 2번 까지 사용할 수 있음.
            arr[s] = set_nums[i]
            cnt_nums[i] -= 1
            recur(s+1)
            cnt_nums[i] += 1

N, M = map(int, input().split())
nums = list(map(int, input().split()))

set_nums = sorted(list(set(nums))) # 중복 제거를 위해 set() 거쳐준다.
cnt_nums = [0]*len(set_nums) # set_nums 리스트에 i 인덱스의 값은 원래 집합(nums)에 몇번 등장하는지 cnt_nums리스트의 i인덱스에 작성
for i in nums:
    idx = set_nums.index(i)
    cnt_nums[idx] += 1

N = len(set_nums)
arr = [0]*M

recur(0)
```