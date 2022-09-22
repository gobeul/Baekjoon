### 백준 15649번 - N과 M (1)

> 2022/09/22 <br>
> 조합과 순열시리즈 첫번째
> N개에서 M 개 뽑기, 중복없이 + 순서 상관있게

```python
def recur(step):
    if step == M: # step 가 0 부터 1개씩 증가하여 M까지 되면 만든 리스트 출력.
        print(*arr)
        return
    for i in range(1, N+1):
        if not visited[i]:
            arr[step] = i
            visited[i] = True
            recur(step+1)
            visited[i] = False
            
N, M = map(int, input().split())
arr = [0 for _ in range(M)] # M 개 배열 미리 생성, 덮어 쓸거다.
visited = [False]*(N+1) # 중복을 피하기 위한 방문처리 리스트

recur(0)
```