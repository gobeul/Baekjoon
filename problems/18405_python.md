### 백준 18405번 - 경쟁적 감염

> 2022/08/19 <br>
> 무난했던 문제

```python
# 배열 크기 , 바이러스 번호
N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)] # N x N 배열
S, X, Y = map(int, input().split())

delta = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우 델타
visited = [[False]*N for _ in range(N)] # 방문기록
virus = [] # 바이러스 리스트(스택)
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append((arr[i][j],i,j)) # (바이러스 번호,i,j)
            visited[i][j] = True
cnt = 0

while S != cnt:
    virus.sort(reverse=True) # 바이러스 번호순 정렬 (내림차순 후입선출할꺼라서)
    tmp = [] # 임시스택(초기화)
    cnt += 1
    while virus : # 탐색
        num, sti, stj = virus.pop()
        for di, dj in delta:
            mi = di + sti
            mj = dj + stj
            # 인덱스 범위 + 미방문 
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == False:
                visited[mi][mj] = True
                arr[mi][mj] = num
                tmp.append((num,mi,mj))
    virus = tmp[:]

print(arr[X-1][Y-1])
```