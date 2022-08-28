### 백준 9012번 - 괄호

> 2022/08/28 <br>
> 문제 의도는 스택을 이용하는 것이었겠지만...

```python
N = int(input())

for tc in range(N):
    JJ = 0
    VPS = list(input())
    for i in VPS:
        if i == "(" :
            JJ += 1
        else: # i = ")"
            JJ -= 1
        if JJ < 0 :
            print("NO")
            break
    else:
        if JJ != 0 :
            print("NO")
        else:
            print("YES")
```