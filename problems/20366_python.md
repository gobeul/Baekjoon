### 백준 20366번 - 같이 눈사람 만들래?

> 2022/10/25 <br>
> 투포인터를 이용한 풀이<br>
> 정렬된 배열에서 기준점(x, y)을 잡고 그 사이에서 투포인터로 이동해 가며 최적값을 찾았다.


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 1e9

arr.sort()
flag = False

for i in range(N-3):
    for j in range(i+3, N):
        print("df")
        me = arr[i] + arr[j]

        left, right = i+1, j-1
        while left < right :
            you = arr[left] + arr[right]
            tmp = abs(me - you)
            ans = min(tmp, ans)
            if tmp < ans:
                ans = tmp
                
            if me > you :
                left += 1
            elif you > me :
                right -= 1
            else:
                ans = 0
                flag = True
                break
        
        if flag:
            break
    if flag:
        break

print(ans)     
```