### 백준 1504번 - 특정한 최단 경로

> 2022/09/20 <br>
> 1번 노드에서 V번 노드까지의 경로중 x, y 번 노드를 최소 1번 이상 방문한는 최단경로는<br>
> 1 -> x -> y -> N 와 1 -> y -> x -> N 중에서 최단경로이다. (각 화살표는 최단경로)<br>
>  
> 처음에 그래프 최단 경로 == BFS!! 하고 풀었는데 계속 틀리더라, 이유를 생각해보니 노드간의 거리가 재각각이어서<br>
> 불가능 했다. 한번에 노드이동보다 10번의 노드이동이 목적지까지 더 빠른 경우가 있어서 방문처리가 힘들었다.<br>
>
> 다익스트라 알고리즘을 적용하여 문제를 풀어야 했다. <br>
> 일반적인 다익스트라 알고리즘을 참고하여 풀었는데 [블로그 참고](https://techblog-history-younghunjo1.tistory.com/247)<br>
> 이 방법은 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 찾아야하기 때문에 시간 복잡도가 O(V^2) 이다. <br>
> 실제로 이 코드도 오래 걸림 1112ms<br>
>
> 실제로 힙으로 구현한 우선순위 큐를 다익스트라에 적용하면 시간복잡도가 O(ElogV)로 확 개선시킬수 있다고 한다.

```python
"""
1-x-y-N
1-y-x-N
모든 경우의 수는 이 두가지로 압축할 수 있음.
근데 노드간의 거리가 제각각 이기 때문에 BFS로는 최단 거리를 구할 수가 없음
-> 다익스트라를 구현해야함
"""
import sys
input = sys.stdin.readline
from collections import deque

def Dijkstrar(sn, en): # 출발 노드 도착 노드
    visited = [False]*(V+1)
    visited[0], visited[1] = True, True
    distance = [sys.maxsize]*(V+1) # 출발노드부터 거리(거리가 매우 큰 값으로)
    distance[sn] = 0 # 출발노드 0거리 0으로
    cnt = 1 # 방문한 횟수
    while cnt != V+1: # V+1번 방문하면 끝
        for next in lines[sn]:
            distance[next] = min(distance[next], distance[sn]+Distance[sn][next]) # next노드까지의 최소경로 업데이트
        
        sn = small_distance_node(visited, distance) # 다음 방문할 노드
        visited[sn] = True
        cnt += 1

    return distance[en] # sn -> en 의 최소 거리 값


def small_distance_node(visited, distance): # 방문하지 않은 노드들 중에 거리가 최소인 노드 반환
    min_dis = sys.maxsize
    min_idx = 0
    for i in range(1, V+1):
        if not visited[i] and distance[i] < min_dis:
            min_dis = distance[i]
            min_idx = i
    
    return min_idx

        
def tmp_BFS(): # 원하는 노드 방문이 가능 한지 확인하는 Dijkstrar
    tmp_visit = [False]*(V+1)
    tmp_visit[0], tmp_visit[1] = True, True
    tmp_q = deque([1])

    while tmp_q:
        node = tmp_q.popleft()
        for next_node in lines[node]:
            if not tmp_visit[next_node]:
                tmp_q.append(next_node)
                tmp_visit[next_node] = True
    
    if tmp_visit[V] and tmp_visit[essential1] and tmp_visit[essential2]:
        return True
    else:
        return False


V, E = map(int, input().split())

lines = [[] for _ in range(V+1)]
Distance = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    lines[s].append(e)
    lines[e].append(s)
    Distance[s][e] = d
    Distance[e][s] = d

essential1, essential2 = map(int, input().split())

if tmp_BFS():
    ans1 = Dijkstrar(1, essential1) + Dijkstrar(essential1, essential2) + Dijkstrar(essential2, V)
    ans2 = Dijkstrar(1, essential2) + Dijkstrar(essential2, essential1) + Dijkstrar(essential1, V)
    print(min(ans1, ans2))

else:
    print(-1)
```