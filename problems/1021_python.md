### 백준 1012번 - 유기농 배추

> 2022/08/19 <br>
> 

```python
cc = int(input())
ans = []
for tc in range(cc):
    #가로 세로 배추위치
    M, N, K = map(int, input().split())

    delta = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우 델타

    visited = [[False]*N for _ in range(M)] # 방문체크
    pos = [] # 배추위치
    for _ in range(K):
        (i, j) = map(int, input().split())
        pos.append((i,j))
    cnt = 0 # 애벌래
    for ii, jj in pos:
        stack = [(ii,jj)] # 스택
        if visited[ii][jj] == False : # 미방문이면
            visited[ii][jj] = True # 방문등록
            cnt += 1 # 애벌레 추가.
        while stack:
            sti, stj = stack.pop()
            for di, dj in delta:
                mi = di + sti
                mj = dj + stj
                # 인덱스 범위 + 미방문 + 배추자리
                if 0 <= mi < M and 0 <= mj < N and visited[mi][mj] == False and (mi, mj) in pos :
                    visited[mi][mj] = True
                    stack.append((mi,mj))
    ans.append(cnt)

for i in ans:
    print(i)
```