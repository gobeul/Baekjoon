### 백준 1074번 - Z

> 2022/08/09 <br>
> N 크기를 줄여가며 재귀를 진행할때 2,3,4 사분면 같은경우는 인덱스를 추가적으로 더해주고 N의 크기를 줄여주며 풀어야 한다.

```python
def ZZ(N, r, c):
    if N == 1:
        a = [[0, 1], [2, 3]]
        return a[r][c]
    
    if r < 2**(N-1) and c < 2**(N-1) : # 1사분면에 있으면
        return ZZ(N-1, r, c) # N 만 줄여서 재귀
    elif r < 2**(N-1) and c >= 2**(N-1) : # 2사분면에 있으면
        return ZZ(N-1, r, c - 2**(N-1)) + 4**(N-1) * 1 # 열 줄이고 번호 더하기
    elif r >= 2**(N-1) and c < 2**(N-1): # 3사분면
        return ZZ(N-1, r - 2**(N-1), c) + 4**(N-1) * 2
    else: # 4사분면
        return ZZ(N-1, r - 2**(N-1), c - 2**(N-1)) + 4**(N-1) * 3
 
N, r, c = map(int, input().split())
print(ZZ(N, r, c))
```