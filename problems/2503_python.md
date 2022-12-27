### 백준 2503번 - 숫자 야구

> 2022/12/27 <br>
> 3자리 숫자의 경우의수를 모두 뽑아놓고 - 조합<br>
> 조건에 따라 소거해 가는 방법으로 풀었다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

# 모든 경우의 수 만들기
def recur(s, lst=[]):
    if s == 3:
        ans.append(lst)
        return
    
    for i in range(1, 10):
        if not visited[i]:
            visited[i] = True
            recur(s+1, lst+[i])
            visited[i] = False

def check(call, s, b):
    tmp = []
    for lst in ans:
        # 개수 확인 볼 + 스트라이크
        if len(set(lst) & set(call)) != s+b:
            continue
        
        # 스트라이크 확인
        c = 0
        for i in range(3):
            if lst[i] == call[i]:
                c += 1
        if c == s:
            tmp.append(lst)
    return tmp       


visited = [False]*10
ans = []
recur(0)

N = int(input())
for _ in range(N):
    call, s, b = input().split()
    call = list(map(int, call))
    ans = check(call, int(s), int(b))

print(len(ans))

```