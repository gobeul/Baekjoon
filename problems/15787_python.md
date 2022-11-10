### 백준 15787번 - 기차가 어둠을 헤지고 은하수를

> 2022/11/10 <br>
> 비트연산자를 활용해 볼 수 있는 아주 좋은 문제였다!!<br>

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def make_hash():
    for i in range(tb):
        v = 1
        for idx, B in enumerate(trains[i], 1):
            if B:
                v *= (idx + 17)**3
        trains[i] = v


tb, cc = map(int, input().split())
trains = [0 for _ in range(tb)]  # 초기 0 -> bit 0000
full20 = 2**20 - 1 # 1111...111 
for _ in range(cc):
    num, *v = map(int, input().split())
    
    if num == 1: # v = [i, x]
        trains[v[0]-1] |= 2**(v[1]-1)
    elif num == 2:
        trains[v[0]-1] &= ~(2**(v[1]-1))
    elif num == 3: # v = [i]
        trains[v[0]-1] = (trains[v[0]-1] << 1) & full20
    else: # num == 4
        trains[v[0]-1] = (trains[v[0]-1] >> 1) & full20

print(len(set(trains)))
```