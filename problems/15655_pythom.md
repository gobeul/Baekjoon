### 백준 15655번 - N과 M (6)

> 2022/09/23 <br>
> 조합과 순열시리즈 여섯번째
> 임의로 주어진 원소에서 N개에서 M 개 뽑기, 중복불가 + 수열내의 순서는 오름차순

```python
def recur(s, last): # 수열내의 순서를 오름차순으로 잡기위해 인덱스는 항상 전보다 큰 값을 가지도록
    if s == M:
        print(*arr)
        return
    
    for i in range(last+1, N):
        if not used[i]:
            arr[s] = nums[i]
            used[i] = True
            recur(s+1, i)
            used[i] = False



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False]*N
arr = [0]*M

recur(0, -1)
```