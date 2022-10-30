### 백준 20922번 - 겹치는 건 싫어

> 2022/10/30 <br>
> 딕셔너리로 숫자의 인덱스를 리스트 형태로 저장해 중복 개수는 리스트의 길이로 카운트, 포인터의 이동은 리스트의 첫번째 원소 +1 이동으로 해결했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

i, ans = 0, 0
while i != N:
    dict = {}
    length = 0
    while i != N:
        num = arr[i]
        try:
            dict[num].append(i)
        except:
            dict[num] = [i]
        
        if len(dict[num]) > K:
            i = dict[num][0] + 1
            ans = max(length,ans)
            break

        i += 1
        length += 1

print(max(ans, length))
```