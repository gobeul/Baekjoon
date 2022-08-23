```python
def ff(s, N): # start팀으로 가능한 인덱스들
    global ans
    if s == N//2 -1:
        tmp = point(ST, N)
        if tmp == 0:
            print(0)
            quit()
        if ans > tmp:
            ans = tmp
        return

    for j in range(ST[0], N):
        if j > ST[-1]: # 중복을 피하기 위해 큰수만 집어넣는다.
            ST.append(j)
            ff(s+1, N)
            ST.pop()


def point(ST, N): # start팀 을 기준으로 link팀 정하고 점수계산
    sp = 0
    lp = 0
    LT = []
    for i in range(N):
        if not i in ST:
            LT.append(i)
    
    for i in ST:
        for j in ST:
            sp += ability[i][j]
    for i in LT:
        for j in LT:
            lp += ability[i][j]
    return abs(sp - lp)


ST = []
N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

ans = 100000000
# start팀의 첫번째 선수, N//2 이후는 스타트 팀하고 링크 팀하고 바뀌는 거라 의미 없음 예) [0,1,2] 하고 [3,4,5]는 중복
for i in range(N//2):
    ST = [i]
    ff(0, N)
    
print(ans)
```