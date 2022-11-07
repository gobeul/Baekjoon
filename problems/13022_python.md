### 백준 13022번 - 늑대와 올바른 단어

> 2022/11/04 <br>
> 크게 어려움이 없던 구현문제<br>
> 단지 `input = sys.stdin.readline ` 사용시에 input() 으로 문자열을 받는 다면 개행문자에 주의하자.

```python
import sys
input = sys.stdin.readline

def find_s(s):
    global idx
    
    cnt = 0
    while idx < len(string):
        if string[idx] == s:
            cnt += 1
            idx += 1

        else:
            return cnt
    return cnt
    

def solve():
    global idx
    
    while idx < len(string):
        cnt = find_s('w') # w 개수 카운트
        if cnt == 0:
            print(0)
            return 

        for s in wolf:
            v = find_s(s)
            if v != cnt:
                print(0)
                return
    print(1)
    return 
    

wolf = ['o', 'l', 'f'] # w 빼고
string = input().rstrip()
idx = 0

solve()
```