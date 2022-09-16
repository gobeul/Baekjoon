### 백준 1167번 - 트리의 지름

> 2022/09/16 <br>
> 트리 구조에서 가장 긴 경로를 구할때 임이의 노드를 하나 정해 그곳에서 가장 긴 노드를 찾고<br>
> 다시 그 노드에서 가장긴 노드를 찾으면 그 길이가 전체 트리에서 가장 긴 길이의 경로가 된다. 

```python
import sys
input = sys.stdin.readline

def DFS(num):
    ans = 0
    visied = [False]*(V+1)
    visied[num] = True
    stack = [(num,0)]

    while stack:
        num, dis = stack.pop()
        if dis > ans:
            ans = dis
            ans_num = num
        for n, d in p[num]:
            if not visied[n]:
                visied[n] = True
                stack.append((n, dis+d))
    
    return [ans_num, ans]


V = int(input())
p = [[] for _ in range(V+1)]

for i in range(V):
    info = list(map(int, input().split()))
    for j in range(1, len(info), 2):
        if info[j] == -1:
            break
        p[info[0]].append((info[j], info[j+1])) # 노드 번호와 거리 정보

tmp = DFS(1) # 임이의 노드(1번)에서 가장 멀리 있는 노드 찾기
ans = DFS(tmp[0]) # 위에서 찾은 노드 기준으로 가장 긴 길이 찾기
print(ans[1])
```