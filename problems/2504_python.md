### 백준 2504번 - 괄호의 값

> 2022/10/19 <br>
> 그냥 스택을 이용한 괄호 판단 문제의 유형 이겠거니 하고 쉽게 봤다가 정말 오래 헤맸다<br>
> 괄호를 보면서 값을 계산하는 부분을 숫자역시 스택에 추가해 줌으로서 해결 할 수 있었다.<br>
> 계산과 동시에 잘못된 괄호의 판단 여부를 같이 실행하려 했으나 코드가 너무 너저분해져 올바른 괄호판단은 따로 빼서 처리했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def check(str):
    stack = []
    for i in range(n):
        if str[i] == '(' or str[i] == '[' :
            stack.append(str[i])
        else:
            if not stack:
                return False
            k = stack.pop()
            if dict[k][0] != str[i]:
                return False
    if stack:
        return False
    return True


dict = {
    '[' : [']', 3],
    '(' : [')', 2],
}

str = input()
n = len(str)

flag = check(str)

stack, i = [], 0
while flag and i != n:
    if str[i] == '(' or str[i] == '[' :
        stack.append(str[i]) # 여는 괄호는 스택에 추가
    else:
        tmp = 0
        while 1:
            k = stack.pop()
            if type(k) == int : # 숫자면
                tmp += k
            else:
                break
        # k 가 여는 괄호고
        if tmp: # 더해준 값이 있었으면 곱하기
            stack.append(tmp*dict[k][1])
        else: # 없으면 괄호값
            stack.append(dict[k][1])
        
    i += 1

print(sum(stack))
```