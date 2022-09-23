### 백준 15652번 - N과 M (4)

> 2022/09/23 <br>
> 조합과 순열시리즈 네번째
> N개에서 M 개 뽑기, 중복허용 + 오름차순

```python
def recur(s, last): # 오름 차순을 위해 last 변수를 정
    if s == M:
        print(*arr)
        return
    
    for i in range(last, N+1): # 중복 및 오름차순을 위해 시작은 last 부터
        arr[s] = i
        recur(s+1, i)

N, M = map(int, input().split())
arr = [0]*M

recur(0, 1)
```