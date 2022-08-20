### 백준 14888번 - 연산자 끼워넣기

> 2022/08/20 <br>
> int(a/b) 와 a//b 는 다르게 계산될 수 있다<br>
> 

```python
def DFS(i, value, a, b, c, d): # i == 1, value == num[0]
    global ans1, ans2
    if i == N:
        if ans1 < value :
            ans1 = value
        if ans2 > value :
            ans2 = value
        return
    if a : # + 가 있으면
        DFS(i+1, value + num[i], a-1, b, c, d)
    if b :
        DFS(i+1, value - num[i], a, b-1, c, d)
    if c :
        DFS(i+1, value * num[i], a, b, c-1, d)
    if d :
        DFS(i+1, int(value/num[i]), a, b, c, d-1)
    
N = int(input()) # 숫자 개수 == 기호 게수+1
num = list(map(int, input().split())) # 수열 리스트
oper = list(map(int, input().split())) # 기호 리스트 
# a, b, c, d == +, -, x, %
a, b, c, d = oper[0], oper[1], oper[2], oper[3]

ans1 = -1000000000 # 가장 큰수
ans2 = 1000000000 # 가장 작은 수

DFS(1, num[0], a, b, c, d)

print(ans1)
print(ans2)
```