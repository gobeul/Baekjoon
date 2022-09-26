### 백준 9663번 - N-Queen

> 2022/09/26 <br>
> pypy로 겨우 시간 안에 통과했다.
> 배열을 2차원으로 만들지 않고 그 행에서의 1차열을 만들고 다음 행으로 넘어갈때 마다 왼쪽 대각선은 인덱스가 -1, 오른쪽 대각선은 인덱스가 +1 이 됨을 이용했다.

```python
def Queen(s, mid, left, right):
    global ans
    if s == N:
        ans += 1
        return 

    visited = [False]*N
    for i in range(s):
        left[i] -= 1
        right[i] += 1
        if left[i] >= 0:
            visited[left[i]] = True
        if right[i] <= N-1:
            visited[right[i]] = True
        visited[mid[i]] = True
        
        
    for i in range(N):
        if not visited[i]:
            Queen(s+1, mid+[i], left+[i], right+[i]) 

N = int(input())
ans = 0

Queen(0, [], [], [])

print(ans)
```