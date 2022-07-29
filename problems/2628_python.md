### 백준 2628번 - 종이자르기

> 2022/07/29 <br>
> 

```python
a, b = map(int, input().split())

n = int(input())
W = [a]
H = [b]
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        H.append(b)
    else:
        W.append(b)

W.sort()
H.sort()
len_w = [W[0]]
len_h = [H[0]]

for i in range(1, len(W)):
    len_w.append(W[i] - W[i-1])

for i in range(1, len(H)):
    len_h.append(H[i] - H[i-1])

ans = []
for i in range(len(len_w)):
    for j in range(len(len_h)):
        ans.append(len_w[i]*len_h[j])

print(max(ans))
```