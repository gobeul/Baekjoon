### 백준 14696번 - 딱지놀이

> 2022/08/03 <br>
> 딱지 모양 순서대로 숫자를 부여하고 이를 합산하여 비교하는 방법으로 계산했다.

```python
def disk_value(n_list):
    for i, v in enumerate(n_list):
        if v == 4:
            n_list[i] *= 10**6
        elif v == 3:
            n_list[i] *= 10**4
        elif v == 2:
            n_list[i] *= 10**2
    return sum(n_list)
    

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    A = disk_value(a[1:])
    B = disk_value(b[1:])

    if A > B:
        print("A")
    elif B > A:
        print("B")
    else:
        print("D")
```