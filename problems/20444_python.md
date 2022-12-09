### 백준 20444번 - 색종이와 가위

> 2022/12/09 <br>
> 절반만 봐도 되는 이유는 곱연산이고 한놈이 줄면 한놈이 늘어서 대칭을 이류기 때문!


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

# 색종이의 총 개수 == (가로 자른 횟수 +1)*(세로 자른 횟수 +1)
# 총 자른 횟수가 정해져 있음

def solve():
    e = N // 2 + 1
    s = 0

    while s <= e:
        # 세로로 자른 횟수
        h = (s + e) // 2
        # 가로로 자른 횟수
        w = N - h
        # 색종이 개수
        c = (h+1)*(w+1)
        
        if c < K :
            s = h+1
        elif c > K :
            e = h-1
        else:
            print('YES')
            return
    
    print('NO')

        
N, K = map(int, input().split())
solve()
```