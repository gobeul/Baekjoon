### 백준 14500번 - 테트로미노

> 2022/09/13 <br>
> 완전 하드코딩으로.. 시간도 7564ms 가 나왔다. 정말 턱걸이로 통과한듯

```python
import sys
input = sys.stdin.readline

def is_scope(i, j):
    if 0 <= i < N and 0<= j < M :
        return True
    return False

def block_1(i, j): # 일자 블럭
    global ans
    a = [(i,j), (i,j-1), (i,j-2), (i,j-3)]
    b = [(i,j), (i,j+1), (i,j+2), (i,j+3)]
    c = [(i,j), (i-1,j), (i-2,j), (i-3,j)]
    d = [(i,j), (i+1,j), (i+2,j), (i+3,j)]

    for case in [a, b, c, d]:
        v = 0
        for mi, mj in case:
            if is_scope(mi, mj):
                v += arr[mi][mj]
            else:
                break
        else:
            if ans < v :
                ans = v

def block_2(i, j): # 네모 블럭
    global ans
    a = [(i,j), (i, j+1), (i+1,j), (i+1,j+1)]
    b = [(i,j), (i, j-1), (i+1,j), (i+1,j-1)]
    c = [(i,j), (i, j+1), (i-1,j), (i-1,j+1)]
    d = [(i,j), (i, j-1), (i-1,j), (i-1,j-1)]

    for case in [a, b, c, d]:
        v = 0
        for mi, mj in case:
            if is_scope(mi, mj):
                v += arr[mi][mj]
            else:
                break
        else:
            if ans < v :
                ans = v

def block_3(i, j): # ㄴ 블럭
    global ans
    a = [(i,j), (i-1,j), (i-2,j), (i,j+1)]
    ar = [(i,j), (i-1,j), (i-2,j), (i,j-1)]
    b = [(i,j), (i,j+1), (i,j+2), (i+1,j)]
    br = [(i,j), (i,j+1), (i,j+2), (i-1,j)]
    c = [(i,j), (i+1,j), (i+2,j), (i,j-1)]
    cr = [(i,j), (i+1,j), (i+2,j), (i,j+1)]
    d = [(i,j), (i,j-1), (i,j-2), (i-1,j)]
    dr = [(i,j), (i,j-1), (i,j-2), (i+1,j)]

    for case in [a, b, c, d, ar, br, cr, dr]:
        v = 0
        for mi, mj in case:
            if is_scope(mi, mj):
                v += arr[mi][mj]
            else:
                break
        else:
            if ans < v :
                ans = v

def block_4(i, j): #번개? 블럭
    global ans
    a = [(i,j), (i-1,j), (i-1, j-1), (i-2, j-1)]
    ar = [(i,j), (i-1,j), (i-1, j+1), (i-2, j+1)]
    b = [(i,j), (i,j+1), (i-1, j+1), (i-1, j+2)]
    br = [(i,j), (i,j+1), (i+1, j+1), (i+1, j+2)]
    c = [(i,j), (i+1,j), (i+1, j+1), (i+2, j+1)]
    cr = [(i,j), (i+1,j), (i+1, j-1), (i+2, j-1)]
    d = [(i,j), (i,j-1), (i+1, j-1), (i+1, j-2)]
    dr = [(i,j), (i,j-1), (i-1, j-1), (i-1, j-2)]

    for case in [a, b, c, d, ar, br, cr, dr]:
        v = 0
        for mi, mj in case:
            if is_scope(mi, mj):
                v += arr[mi][mj]
            else:
                break
        else:
            if ans < v :
                ans = v

def block_5(i, j): # ㅗ 블럭
    global ans
    a = [(i,j), (i-1,j), (i,j+1), (i,j-1)]
    b = [(i,j), (i-1,j), (i+1,j), (i,j+1)]
    c = [(i,j), (i+1,j), (i,j+1), (i,j-1)]
    d = [(i,j), (i-1,j), (i+1,j), (i,j-1)]

    for case in [a, b, c, d]:
        v = 0
        for mi, mj in case:
            if is_scope(mi, mj):
                v += arr[mi][mj]
            else:
                break
        else:
            if ans < v :
                ans = v

N, M = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(N) ]
ans = 0

for i in range(N):
    for j in range(M):
        block_1(i,j)
        block_2(i,j)
        block_3(i,j)
        block_4(i,j)
        block_5(i,j)

print(ans)
```