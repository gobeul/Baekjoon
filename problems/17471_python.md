### 백준 17471번 - 게리맨더링

> 2022/08/28 <br>
> 2진탐색으로 부분집합을 구한다 = 선거구A<br>
> 선거구A 를 제외한 나머지를 선거구B로 둔다.<br>
> 각각 BFS를 이용해 연결됐는지 확인하고 연결됐다면 인원수차이를 저장한다.<br>
> 저장한 값중에서 최소값을 출력한다.

```python
"""
선거구를 나눌 수 있는 경우의 수를 모두 구한다 .
-> 각각의 경우에 대해 모두 BFS 를 돌려서 연결이 되어있는지 확인한다.
-> 연결이 확인되면 두 구의 인구수 차이를 기록한다.
-> 기록이 모두 끝나면 그 중 최소값을 출력한다.
"""

def reverse(arr, N): # 선구구 번호를 리스트를 받으면 그 반대 선거구 리스트를 줌
    r = []
    for i in range(1, N+1):
        if i not in arr:
            r.append(i)
    return r 

def BFS(stack, arr):
    if stack == []:
        return

    a = stack.pop()
    for t in line[a]:
        if visited[t] == False and t in arr:
            visited[t] = True
            stack.append(t)
    return BFS(stack, arr)

def Check(arr): # BFS 돌고 다 연결됐는지 확인
    for i in arr:
        if visited[i] == False:
            return False
    
    return True


N = int(input())
population = [0] # 인구수 1번 ~ N번
population += list(map(int, input().split()))

total_population = sum(population) # 전체 인구수
ans = [] # 선거구 인구 차이 담을 리스트

line = [[]] # 연결 관계도 1 ~ N 번
for i in range(1, N+1):
    n, *a = map(int, input().split())
    line.append(a)

c = 0 # 선거구 나눌 수 없는 경우 [] 가 3개 이상 (0번 인덱스 포함이라 3개)
for i in line:
    if i == []:
        c += 1
        if c == 3 and N != 2: # N == 2이면 선거구 연결의 없어도 됨
            print(-1)
            quit()

combi = [] # 조합 가능한 경우의 수 (부분집합)
for i in range(1<<N):
    tmp = []
    for j in range(N):
        if i & (1<<j):
            tmp.append(j+1)
    combi.append(tmp)

for i in combi:
    k = len(i)
    if k == 0 or k == N: # 선거구가 0개 이거나 전체 이거나
        continue
    j = reverse(i, N) # 반대 선거구 리스트
    visited = [False] * (N+1) # 방문기록 초기화
    visited[0] = True # 0번은 없는거라서 방문처리

    # i 선거구 연결 확인
    stack = [i[0]]
    visited[i[0]] = True
    BFS(stack, i)

    if Check(i) == False :
        continue

    #j 선거구 확인
    stack = [j[0]]
    visited[j[0]] = True
    BFS(stack, j)

    if Check(j) == False :
        continue

    # 다 연결 됐다면
    v = 0
    for p in i:
        v += population[p]
    ans.append(abs(total_population - v*2)) # 두 선거구 인원수 차이를 저장
    if total_population == v*2: # 최소 인원차 0이라면 종료
        print(0)
        quit()

try: # ans 가 비어있어서 (= 연결되는 선거구가 없어서) 오류가 나면
    print(min(ans)) 
except: # -1 을 출력
    print(-1)
```