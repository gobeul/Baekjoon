### 백준 23037번 - 5의 수난

> 2022/07/19 <br>


```python
n_list = list(map(str, input()))

ans = 0
for i in n_list:
    ans += int(i)**5
print(ans)
```