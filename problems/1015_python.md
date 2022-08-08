### 백준 1015번 - 수열 정렬

> 2022/08/08 <br>
> 인덱스 관계가 얽혀서 헷갈렸던 문제였다.

```python
n = int(input())

A = list(map(int, input().split()))
P = [0]*n # P는 A와 길이가 같다.

B = sorted(A)

for i in range(n):
    P[A.index(B[i])] = i
    A[A.index(B[i])] = -1 # 중복된 숫자를 처리하기 위해서
print(*P)
```