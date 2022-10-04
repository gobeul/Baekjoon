### 백준 17135번 - 캐슬 디펜스

> 2022/10/04 <br>
> 조합 + BFS + 구현문제<br>
> BFS를 사용할 때 visited 의 방문처리가 따로 필요하지 않았다. 우선순위를 잘 고려해 델타 순서만으로 해결이 가능했다.<br>
> 적이 매번 한칸씩 내려오는 것 대신 사정거리를 1 늘리고 밑에서 부터 한 행씩 제외하는 방법을 사용했는데 다른 사람 코드를 보니 이방법이 더 느린것 같았다.

```python
import sys
from collections import deque
input = sys.stdin.readline

"""
적이 한칸씩 내려오는걸 매번 구현하기엔 제약이 있어보임
-> 매턴 D의 범위를 늘려가는건 어떨까
 D += 1 하고 N 번째 줄 제외
 D += 1 하고 N-1 번째 줄까지 제외
 ...
"""

def in_range(si, sj, ei, ej): # 사정거리 내인가
    k = abs(si-ei) + abs(sj - ej)
    if k <= R:
        return True
    return False

def recur(s, last):
    if s == 3:
        archer.append(tmp[:])
        return
    
    for i in range(last+1, M):
        tmp[s] = i
        recur(s+1, i)

def BFS(i, j): # 궁수 좌표와 턴수로 적 찾기
    bfs_visit = [[False]*M for _ in range(N)]
    si, sj = i, j # 현재궁수 좌표
    que = deque([(i, j)])

    while que:
        i, j = que.popleft()
        for di, dj in delta:
            mi, mj = i+di, j+dj
            # 인덱스 벙위, 사정거리
            if 0 <= mi < N and 0 <= mj < M and not bfs_visit[mi][mj]:
                # 적이고 사정거리 내 이고, 사라진 적이 아닌지, 이미 처치한 적이 아닌지
                if arr[mi][mj] == 1 and in_range(si,sj,mi,mj) and mi < turn and not visited[mi][mj]:
                    enemy.add((mi, mj)) # 적 목록에 추가
                    return # 바로 리턴하면 최단거리 적이 된다.

                bfs_visit[mi][mj] = True
                que.append((mi,mj))

delta = [(0,-1), (-1,0), (0,1)] # 델타 3방향, 왼 위 오

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

archer = [] # 궁수 위치 좌표(열좌표)
tmp = [-1,-1,-1]
recur(0, -1) # 궁수 위치 좌표 뽑기

ans = 0
for c1, c2, c3 in archer: # 모든 궁수의 좌표값의 경우에 대해서
    visited = [[False]*M for _ in range(N)] # 처치 기록
    tmp_ans = 0 # 총 처치한 적 수
    turn = N # 턴수
    R = D # 사정거리
    tmp_archer = [(N, c1), (N, c2), (N, c3)] # 궁수 좌표
    while turn : # turn == 0 이되면 종료
        enemy = set() # 적 좌표
        for ai, aj in tmp_archer:
            BFS(ai, aj)
        
        for ei, ej in enemy:
            tmp_ans += 1
            visited[ei][ej] = True
        
        turn -= 1 # 턴수 감소 및 사정거리 증가
        R += 1
    
    ans = max(ans, tmp_ans) # 최대값 갱신

print(ans)
```