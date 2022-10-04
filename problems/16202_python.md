### 백준 16202번 - MST 게임

> 2022/10/03 <br>
> 최소신장트리 MST 를 구하는 알고리즘으로 prim 을 사용해 봤다.<br>
> prime 은 매번 최소의 경로를 선택하므로 매 턴수 마다 값을 최소 간선을 빼줄때 그냥 K_turn 리스트에 들어온 순서대로 빼주면 됐다.<br>
>
> 사실 prim 은 시간 복잡도가 O(N^2)으로 python3 로는 시간초과를 피할 수 없었고 해당코드는 pypy3 로 통과했다.<br>
> python3 로 통과하기 위해서 prim 대신 kruskal 을 사용하면 될듯하다.
  
```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def prim(start):
    dis = [inf]*(V+1)
    visited = [False]*(V+1)
    dis[start] = 0

    for _ in range(V):
        idx = 0
        minV = inf
        for i in range(1, V+1):
            if not visited[i] and minV > dis[i]:
                idx = i
                minV = dis[i]
        
        visited[idx] = True

        for next in range(1, V+1):
            if not visited[next] and arr[idx][next]:
                if dis[next] > arr[idx][next]:
                    dis[next] = arr[idx][next]   
    
    return sum(dis[start:])
        

V, M, K = map(int, input().split()) # 노드 , 간선 개수, 턴 수

arr = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
K_turn = []
for d in range(1, M+1):
    s, e = map(int, input().split())
    arr[s][e] = d
    arr[e][s] = d
    K_turn.append((s, e)) # 매턴마다 사라질 최소 가중치 간선

inf = 99999999999

fail = False 
for i in range(K): # K 턴 만큼 진행
    if fail: # 신장 트리가 한번 끊어지면 계속 끊어짐
        print(0, end=" ")
        continue

    tmp = prim(1)
    if tmp < inf:
        print(tmp, end=" ")
        ds, de = K_turn[i]
        arr[ds][de] = 0
        arr[de][ds] = 0 # 간선 끊기
    else:
        print(0, end=" ")
        fail = True
print()
```