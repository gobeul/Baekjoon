### 백준 1245번 - 농장 관리
> 2022/12/27 <br>
> DFS 방식으로 배열을 탐색하며 해결했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def solve():
        
    def isRange(i, j):
        if 0 <= i < N and 0 <= j < M:
            return True
        return False

    # 봉우리 check 안해도 될 좌표 확인하기
    def updatePeak(i, j, v):
        stack = [(i, j, v)]
        while stack:
            si, sj, p = stack.pop()
            for di, dj in delta:
                mi = si + di
                mj = sj + dj
                if isRange(mi, mj) and peak[mi][mj] and arr[mi][mj] <= p:
                    peak[mi][mj] = False
                    stack.append((mi, mj, arr[mi][mj]))


    # v 높이의 (i, j)가 봉우리가 될 수 있는가??
    def check(i, j, v): # 봉우리 좌표, 봉우리 높이
        stack = [(i, j)]
        peak[i][j] = False
        while stack:
            si, sj = stack.pop()
            for di, dj in delta:
                mi = si + di
                mj = sj + dj
                if not isRange(mi, mj):
                    continue

                if arr[mi][mj] > v: # 더 높은게 있는 경우
                    return False # 봉우리 될 수 없음
        
                elif arr[mi][mj] == v and peak[mi][mj]: # 같은 높이 이고 visited 가 아직 False 라면
                    return False
                
                # 낮다면 pass
                # else:
                #     pass
        
        updatePeak(i, j, v)
        return True

    delta = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)] # 8 방향 델타

    N, M = map(int, input().split()) # N : 행 // M : 열
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 정보

    peak = [[True]*M for _ in range(N)] # 봉우리 가능성이 있는 애들
    ans = 0 # 봉우리 개수
    for i in range(N):
        for j in range(M):
            # 높이가 1이상 + 가능성(peak) + 봉우리 체크(check)
            if arr[i][j] and peak[i][j] and check(i, j, arr[i][j]):
                ans += 1

    print(ans)

solve()
            
```