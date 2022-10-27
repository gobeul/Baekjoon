### 백준 2615번 - 오목

> 2022/10/27 <br>
> 배열을 보면서 돌이 옿인 위치부터 8방향의 오목 여부를 판단하는 방법으로 풀이했다.<br>
> 불필요한 방향까지 모두 탐색하기에 시간이 많이 걸릴줄 알았는데 그렇지 않았다.<br>
> 19x19 배열로 워낙 작아서 그런것같다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def is_range(i, j):
    if 0 <= i < 19 and 0 <= j < 19 :
        return True
    return False

def check(si, sj, c):
    global dir
    for di, dj in delta:
        i, j = si, sj
        # 6목 부분 먼저 체크
        if is_range(i-di, j-dj) and arr[i-di][j-dj] == c:
            continue
        if is_range(i+di*5, j+dj*5) and arr[i+di*5][j+dj*5] == c:
            continue
        tmp = [(si, sj)] # 돌 모으기
        for k in range(1, 5):
            mi, mj = di*k + i, dj*k + j
            tmp.append((mi,mj))
            if not is_range(mi, mj) or arr[mi][mj] != c:
                break
        else:
            return tmp

    return False


def solve():
    for i in range(19):
        for j in range(19):
            if arr[i][j]:
                tmp =  check(i, j, arr[i][j])
                if tmp:
                    tmp.sort(key = lambda x : (x[1], x[0]))
                    print(arr[i][j])
                    print(tmp[0][0]+1, tmp[0][1]+1)
                    return

    print(0)
    return


delta = [(0,-1), (0,1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1) ] # 8방향
arr = [list(map(int, input().split())) for _ in range(19)]
dir = 0

solve()
```
