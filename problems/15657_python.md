### 백준 15657번 - N과 M (8)

> 2022/09/23 <br>
> 조합과 순열시리즈 여덟번째
> 임의로 주어진 원소에서 N개에서 M 개 뽑기, 중복허용 + 수열 자체는 오름차순 + 전체 출력은 사전순으로
  
```python
def recur(s, last):
    if s == M:
        print(*arr)
        return

    for i in range(last, N):
        arr[s] = nums[i]
        recur(s+1, i)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = [0]*M

recur(0, 0)
```