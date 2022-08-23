### 백준 1920번 - 수 찾기

> 2022/08/23 <br>
> 이진탐색 문제

```python
def SS(n):
    s = 0
    e = N-1
    
    while s <= e:
        m = (s+e)//2
        if N_list[m] == n:
            print(1)
            return
        elif N_list[m] > n :
            e = m -1
        else:
            s = m +1

    print(0)
    return

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_list.sort() # 이진탐색을 위해서는 리스트의 정렬이 필요하다.
a, b = N_list[0], N_list[-1]

for i in M_list :
    SS(i)
```