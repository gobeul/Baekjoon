### 백준 16637번 - 괄호 추가하기

> 2022/11/06 <br>
> 조합으로 모든 괄호의 경우의 수를 확인하여 해결했다.<br>
> 계산은 eval 함수를 사용해 보았다.<br>
> 일반 적인 사칙연산의 우선순위가 적용되지 않아 생각을 좀 더 해봐야 하는 문제였다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import deque


def calculator(lst):
    BB = add_bracket(lst)
    que = deque(BB)

    tmp = ''
    for k in range(7):
        s = que.popleft()
        tmp += s
        if k == 2 and s != '(': # 괄호가 있다면 3번째는 괄호가 온다.
            break
    tmp = str(eval(tmp))
    
    while que: # 두번째 부터는 값이 있기 때문에 수식 + 숫자로 결정됨
        for k in range(6):
            s = que.popleft()
            tmp += s
            if k == 1 and s != '(': # 괄호가 있다면 3번째는 괄호가 온다.
                break

        tmp = str(eval(tmp))
    
    return int(tmp)


def add_bracket(lst): # 괄호 추가 하기
    k = -2
    tmp = cal_list
    for idx in lst:
        k += 2 # 괄호가 추가 되면 인덱스가 늘어나니깐
        tmp = tmp[:idx-1+k] + ['('] + tmp[idx-1+k:idx+2+k] + [')'] + tmp[idx+2+k:]
    return tmp


def recur(bracket_list, last): # 괄호 위치 정하기
    global ans

    ans = max(ans, calculator(bracket_list))

    for i in range(last+2, n-1, 2):
        recur(bracket_list+[i], i+2)
    


n = int(input().rstrip())
cal_list = list(input())
if n == 1:
    print(cal_list[0])
else:
    ans = calculator([]) # 초기값 == 괄호 추가 안한 값
    recur([], 1) # 1번 인덱스는 괄호를 씌울 이유가 없음
    print(ans)
```