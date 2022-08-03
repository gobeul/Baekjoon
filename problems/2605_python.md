### 백준 2605번 - 줄 세우기

> 2022/08/02 <br>
> 0 을 뽑으면 제자리(자신의 인덱스), 최대 숫자를 뽑으면 맨 앞자리(인덱스 0) 임을 이용하여 계산했다.

```python
n = int(input())
pick = list(map(int, input().split()))

ans = [i for i in range(1, n+1)]
for i , v in enumerate(pick):
    k = ans.pop(i)
    ans.insert(k-1-v, k)

print(*ans)
```
