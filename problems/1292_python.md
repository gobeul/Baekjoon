### 백준 1292번 - 쉽게 푸는 문제

> 2022/07/18 <br>

```python
a , b = map(int, input().split())

n_list = [0]*(b+1)

cnt = 0 # [0, 1, 2, 2, 3, 3, ..]
v = 1
for i in range(1, b+1):
    n_list[i] = v
    cnt += 1
    if cnt == v :
        cnt = 0
        v += 1

ans = n_list[a:]

print(sum(ans))
```