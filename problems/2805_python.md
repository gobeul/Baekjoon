### 백준 2805번 - 나무 자르기

> 2022/09/06 <br>
> 이진 탐색을 이용해 풀이하였는데 다른 분들보다 시간이 동작시간이 훨씬 길었다 자른 나무 길이를 더하는 과정에서 중복값들은 딕셔러니로 묶어 하나하나 더하지 않고 곱해서 한번에 처리한는 방법으로 줄이신거 같다.


```python
import sys
input = sys.stdin.readline

def cutting(n):
    ans = 0
    for i in tree:
        if i > n:
            ans += i - n
    return ans

N, M = map(int, input().split())
tree = list(map(int, input().split()))

s = 0
e = max(tree)

mid = (s+e)//2

ans = 0
while s <= e:
    k = cutting(mid)

    if k >= M:
        ans = mid
        s = mid + 1

    else:
        e = mid - 1
    
    mid = (s+e)//2

print(ans)
```