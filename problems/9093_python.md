### 백준 9093번 - 단어 뒤집기

> 2022/07/17 <br>



```python
n = int(input())
for i in range(n):
    w_list = list(map(str, input().split()))

    for i in w_list:
        print(i[::-1], end=" ")
    print("")
```
