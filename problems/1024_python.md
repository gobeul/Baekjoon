### 백준 1024번 - 수열의 합

> 2022/08/07 <br>
> l 길이의 수열 부터 모든 경우의 수를 확인해가며 해결했다.

```python
n, l = map(int, input().split())

K = True
while K:
    b_list = [i for i in range((n//l - 50)-1, (n//l + 50)+1) ] # 리스트의 값의 최대값은 n//l + 50+1 을 넘길 수 없다.(l 의 100을 넘길 수 없으므로 50이다.) 
    
    if b_list[0] < 0: # 리스트 값중에 음수가 있다면 제가하는 과정.
        idx = b_list.index(0)
        del b_list[:idx]

    cnt = 0
    while cnt+l <= len(b_list):

        if sum(b_list[cnt : cnt+l]) == n :
            print(*b_list[cnt : cnt+l])
            K = False
            break
        cnt += 1
        # 위에서 값을 찾았을때 l = 100이면 여기서 l = 101 이기떄문에 여기서 걸리지 않도록 K != 100 을 추가 해 준다.
    l += 1
    if l > 100 and K != False :
        print(-1)
        break
```