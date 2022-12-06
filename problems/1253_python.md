### 백준 1253번 - 좋다

> 2022/12/06 <br>
> 두 포인터 문제였는데 N크기가 2000이고 시간제한이 2초나 주어져서 수원하게 풀었다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

good = 0 # 굿 개수
for i in range(N):
    target = arr[i] # 만들 숫자
    left, right = 0, N-1 # 두 포인터

    # i 와 포인터들이 같은 경우 조정
    if i == 0:
        left = 1
    elif i == N-1:
        right = N-2

    while left < right:
        v = arr[left] + arr[right]

        if v > target:
            right -= 1
            if right == i:
                right -= 1
        elif v < target:
            left += 1
            if left == i:
                left += 1
        else: # Good
            good += 1
            break

print(good)
```