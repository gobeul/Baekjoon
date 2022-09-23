### 백준 15654번 - N과 M (5)

> 2022/09/23 <br>
> 조합과 순열시리즈 다섯번째
> 임의로 주어진 원소에서 N개에서 M 개 뽑기, 중복불가 + 순서 상관있게

```python
def recur(s):
    if s == M:
        print(*arr)
        return
    
    for i in range(N):
        if not used[i]:
            arr[s] = nums[i]
            used[i] = True
            recur(s+1)
            used[i] = False



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() # 오름차순을 위한 정렬

used = [False]*N
arr = [0]*M
```