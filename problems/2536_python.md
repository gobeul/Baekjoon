### 백준 2536번 - 버스 갈아타기

> 2022/11/13 <br>
> 코드의 가독성이 너무 떨어져서 인지 수정하기까지의 시간이 너무 오래 걸렸다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque

def busTransfer(busNum): # 현재 노선에서 환승 가능한 버스 찾기
    (m1, s1i, s1j, e1i, e1j) = busList[busNum]
    tmp = []
    for other in range(1, bbb+1):
        (m2, s2i, s2j, e2i, e2j) = busList[other]
        if busNum != other and not busUsed[other]: 
            if m1 == m2: # m : 1 => 수직 이동 // m : 0 => 평행 이동
                if m1 == 1 and s1j == s2j and (min(s1i,e1i) <= s2i <= max(s1i,e1i) or min(s1i,e1i) <= e2i <= max(s1i,e1i) or min(s2i,e2i) <= s1i <= max(s2i,e2i)) :
                    tmp.append(other)
                elif m1 == 0 and s1i == s2i and(min(s1j,e1j) <= s2j <= max(s1j,e1j) or min(s1j,e1j) <= e2j <= max(s1j,e1j) or min(s2j,e2j) <= s1j <= max(s2j,e2j)) :
                    tmp.append(other)

            else:
                if m1 == 1 and min(s1i,e1i) <= s2i <= max(s1i,e1i) and min(s2j,e2j) <= s1j <= max(s2j,e2j):
                    tmp.append(other)
                elif m1 == 0 and max(s1j,e1j) >= s2j >= min(s1j,e1j) and max(s2i,e2i) >= s1i >= min(s2i,e2i):
                    tmp.append(other)

    return tmp

def check(x): # x번 버스 노선에 도착지가 있는가?
    (m, si, sj, ei, ej) = busList[x]
    if si == ei and ei == fei and max(sj,ej) >= fej >= min(sj,ej):
        return True
    elif sj == ej and ej == fej and max(si,ei) >= fei >= min(si,ei):
        return True
    return False

def solve():
    que = deque() # (이용중인 버스 번호, 버스 사용 횟수)
    for i in range(1, bbb+1):
        m, ai, aj, bi, bj = busList[i]
        if min(ai,bi) <= fsi <= max(ai,bi) and min(aj,bj) <= fsj <= max(aj,bj): # 출발지에서 탈 수 있는 버스
            que.append((i, 1))
            busUsed[i] = True

    while que:
        busNum, cnt = que.popleft()
        if check(busNum): # 도착지가 있으면
            return cnt

        # 없으면
        for next in busTransfer(busNum):
            if  not busUsed[next]:
                busUsed[next] = True
                que.append((next, cnt+1))
    
  

m, n = map(int, input().split())
adjust = [i for i in range(n-1, -1, -1)] # i 값 조정용

bbb = int(input())
busList = [0]*(bbb+1) # 버스 출발, 도착 좌표, 방향(수직:0, 수평:1)
busUsed = [False]*(bbb+1) # 같은 버스는 2번 이상이용하지 않는다.

for _ in range(bbb):
    b, x1, y1, x2, y2 = map(int, input().split())
    sj, ej = x1 -1, x2 -1
    si, ei =  adjust[y1-1], adjust[y2-1]

    if si == ei: # 평행이동
        m = 0
    else: # 수직이동
        m = 1

    busList[b] = [m, si, sj, ei, ej]


x1, y1, x2, y2 = map(int, input().split())
fsj, fej = x1 -1, x2 -1
fsi, fei =  adjust[y1-1], adjust[y2-1]


print(solve())
```


