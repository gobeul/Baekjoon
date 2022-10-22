### 백준 21314번 - 민겸 수

> 2022/10/22 <br>
> 어렵지 않게 구현이 가능한 문제였는데 sys.stdin.readline 의 개행문자를 생각치 못해서 왜틀렸는지 한참 고민했던 문제..

```python
def max_num(st):
    idx, cnt, v = 0, 0, "0"
    while idx != N:
        if st[idx] == 'M':
            cnt += 1
        else: # K가 나오면
            v += '5'+'0'*cnt # 앞서 나온 M개수 만큼 0을 붙여줌
            cnt = 0
        idx += 1

    v += '1'*cnt
    return int(v)

def min_num(st):
    idx, cnt, v = 0, 0, "0"
    while idx != N:
        if st[idx] == 'M':
            cnt += 1
        else: # K가 나왔을때
            if cnt: # M 이전에 나왔으면
                v += '1'+'0'*(cnt-1)
            v += '5'
            cnt = 0

        idx += 1
    
    if cnt:
        v += '1'+'0'*(cnt-1)
    return int(v)

st = input()
N = len(st)

print(max_num(st))
print(min_num(st))
```