### 백준 4949번 - 군형잡힌 세상

> 2022/09/05 <br>
> 스택 관련해서 많이 접해본 괄호 문제..!

```python
while 1:
    stence = input()
    stack = []

    if stence == '.':
        break

    for i in stence:
        if i in ['(', '['] :
            stack.append(i)
        
        elif i == ')':
            if not stack:
                print('no')
                break
            if stack[-1] == '(':
                a = stack.pop()
                pass
            else:
                print('no')
                break
        
        elif i == ']':
            if not stack:
                print('no')
                break
            if stack[-1] == '[':
                a = stack.pop()
                pass
            else:
                print('no')
                break
    
    else:
        if stack:
            print('no')
        else:
            print('yes')
```