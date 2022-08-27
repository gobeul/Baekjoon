### 백준 1389번 - 케빈 베이컨의 6단계 법칙

> 2022/08/24 <br>
> 간잔한 BFS 문제.. 였지만.. cnt += 1 의 타이밍을 잘 못생각해서 왜 틀렸는지 꽤 오래 고민했다..!<br>
>deque 모듈로 만든 큐는 슬라이싱이 안됨. 그래서 느리지만 copy()를 사용했다.

```python
from collections import deque

N, M = map(int, input().split())

line = [[] for _ in range(N+1)] # 친구 관계도
for _ in range(M):
    a, b = map(int, input().split())
    line[a].append(b) # 쌍방으로 연결
    line[b].append(a)

ans = [0 for _ in range(N+1)] # 인덱스에 맞춰 케빈 베이컨 수 저장
queue = deque() # 큐 초기화

# BFS
for i in range(1, N+1): # 1번 부터 N 번까지 확인
    visited = [False]*(N+1) # 방문 기록 초기화
    queue.append(i) # i 번 출발
    visited[i] = True # 방문처리
    cnt = 1 # 케빈베이컨 수 초기화
    while queue:
        tmp_q = queue.copy() # cnt += 1 타이밍이 거리 cnt 인 노드를 다 돌아야 해줘야 돼서
        queue = deque()
        while tmp_q:
            st = tmp_q.popleft()
            for j in line[st]:
                if visited[j] == False: # 미방문이면
                    visited[j] = True
                    queue.append(j)
                    ans[i] += cnt
        cnt += 1 # 거리 cnt 노드를 다 처리하면 거리 + 1 해줌

print(ans.index(min(ans[1:]))) # 0 번 인덱스를 제외한 최소값은 가지는 인덱스를 확인함
```