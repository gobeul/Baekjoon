### 백준 2473번 - 세 용액

> 2022/11/08 <br>
> 투포인터 문제<br>
> 세 지점을 구해야 함으로 한개의 인덱스를 고정시키고 남은 구역에서 포인터를 이동 시킨다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

if max(arr) <= 0: # 단순 시간 줄이기 용
    print(arr[N-3], arr[N-2], arr[N-1])
elif min(arr) >= 0: # 단순 시간 줄이기 용
    print(arr[0], arr[1], arr[2])
else:

    val = 9999999999
    for x in range(N-2): # 고정 값
        tmp = arr[x]
        i, j, = x+1, N-1
        while i < j:
            tmp_val = tmp + arr[i] + arr[j]
            if abs(tmp_val) < val:
                val = abs(tmp_val)
                ans = [tmp, arr[i], arr[j]]

            # 포인터 이동 
            if tmp_val < 0:
                i += 1
            elif tmp_val > 0:
                j -= 1
            else: # 0인경우
                print(*ans)
                quit()

    print(*ans)
```