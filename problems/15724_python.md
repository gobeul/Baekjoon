### 백준 15724번 - 주지수

> 2022/11/17<br>
> 이차원배열의 구간합 문제<br>
> 11660번과 같다<br>

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

# 맨 위하고 왼쪽 패딩주기
arr = [[0] for _ in range(N+1)]
arr[0] += [0]*M
for i in range(1, N+1):
    arr[i] += list(map(int, input().split()))

# 구간합 들어갈 배열 + 굳이 새로 만들 필요는 없을 듯
for si in range(1, N+1):
    for sj in range(1, M+1):
        # 구간합 배열 구하기
        # 그 위치 + 위쪽 사각형 + 왼쪽 사각형 - 겹친 사각형
        arr[si][sj] = arr[si][sj] + arr[si-1][sj] + arr[si][sj-1] - arr[si-1][sj-1]

cc = int(input())
for _ in range(cc):
    ans = 0
    si, sj, ei, ej = map(int, input().split())
    ans = arr[ei][ej] # + 마지막 좌표까지 구간합
    ans -= arr[si-1][ej] # - 위쪽 사각형
    ans -= arr[ei][sj-1] # - 왼쪽 사각형
    ans += arr[si-1][sj-1] # + 겹친 사각형
    
    print(ans)
```