### 백준 2635번 - 수 이어가기

> 2022/07/24 <br>
> 예시로 나온 테스트 케이스에 x = N*0.62 를보고 범위를 60%~65% 로 두어 계산했다.<br>
>범위를 지정했을때 72ms // 지정안했을때 92ms 
>
>N의 값이 30,000,000 인 경우도 테스트 해봤는데 이 범위에서 답이 나왔다. 또한 이경우 실행시간에서 상당한 차이가 있었다.

```python
def numberline(N, x, lst):
    if N-x < 0:
        return lst
    lst.append(N-x)
    return numberline(x, N-x, lst)

N = int(input())

a = int(N*0.6)-1
b = int(N*0.65)+1

ans = []
for i in range(a, b+1):
    c = numberline(N, i, [N, i])
    if  len(c) > len(ans):
        ans = c

print(len(ans))
print(*ans)
```