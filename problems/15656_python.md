### 백준 15656번 - N과 M (7)

> 2022/09/23 <br>
> 조합과 순열시리즈 일곱번째
> 임의로 주어진 원소에서 N개에서 M 개 뽑기, 중복허용 + 전체 출력은 사전순으로 

```python
def recur(s): # 15655 문제에서 last 변수만 빠짐 => 중복가능함으로!!
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
nums.sort()

used = [False]*N
arr = [0]*M

recur(0)
```