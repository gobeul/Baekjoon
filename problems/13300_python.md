### 백준 13300번 - 방배정

> 2022/08/03 <br>
> 성별과 학년의 곱으로 모든 학년별 학생을 구분지어 해결했다. (0은 숫자를 바꾸어서 진행)


```python
import math

n, k = map(int, input().split())

info_list =[]
for i in range(n):
    s, g = map(int, input().split())
    if s == 0:
        s = 100

    info_list.append(s*g)

info_set = set(info_list.copy())

ans = 0
for i in info_set:
    p = info_list.count(i)/k
    ans += math.ceil(p)

print(ans)
```