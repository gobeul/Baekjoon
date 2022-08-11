### 백준 10157번 - 자리배정

> 2022/07/31 <br>
> 동서남북 이동에 있어 그방향의 이동이 끝나는 좌표의값을 이용하여 방향을 구분짓고 계산했다.<br>

> 2022/08/10
> 델타를 이용한 2차원 배열 탐색 학습 후 델타를 지정하고 풀어 보았다.<br>
> 코드도 간결해진 느낌이고 시간도 줄었다.(276 -> 84)
```python
W, H = map(int, input().split())
K = int(input())

cnt = 1
ans = [1, 1]
round_cnt = 0
esc = True
if K > W*H :
    print(0)
else:
    while esc:
        if cnt == K:
            break
        if (ans[0] < W/2 +1) and (ans == [1+round_cnt, 1+round_cnt]) : # 위로 이동 시작
            while ans[1] != H-round_cnt:
                ans[1] += 1
                cnt += 1
                if cnt == K:
                    esc = False
                    break
        elif (ans[0] < W/2 +1) and (ans == [1+round_cnt, H-round_cnt]) : #오른쪽으로 이동 시작
            while ans[0] != W-round_cnt:
                ans[0] += 1
                cnt += 1
                if cnt == K:
                    esc = False
                    break
        elif (ans[0] > W/2 -1) and (ans == [W-round_cnt, H-round_cnt]) : # 아래로 이동 시작
            while ans[1] != 1+round_cnt:
                ans[1] -= 1
                cnt += 1
                if cnt == K:
                    esc = False
                    break
        else: #왼쪽으로 이동 시작, 라운드 카운트 += 1 
            round_cnt += 1
            while ans[0] != 1+round_cnt:
                ans[0] -= 1
                cnt += 1
                if cnt == K:
                    esc = False
                    break
            ans[1] +=1
            cnt +=1

    if cnt > K:
        ans[1] -= 1

    print(*ans)
```

----
2022/08/10<br>
배열을 만들 필요가 없다.
```python
N, M = map(int, input().split())
K = int(input())


du = [i for i in range(1, M+1)]
dd = [i for i in range(M, 0, -1)]
dr = [i for i in range(1, N+1)]
dl = [i for i in range(N, 1, -1)] # 왼쪽 방향은 하나 적음

u = True
d, r, l = False, False, False
ans = [1, 1]
cnt = 1

if K > N*M: # K 값이 범위보다 큰 경우2
    print(0)
    quit()

while cnt < K :

    if u: # y축 위로 이동
        cnt += du[-1] - ans[1]
        ans = [ans[0], du[-1]]
        del du[-1]
        u, r = False, True
    
    elif r: #x축 오른쪽 이동
        cnt += dr[-1] - ans[0]
        ans = [dr[-1], ans[1]]
        del dr[-1]
        r, d = False, True
    
    elif d:
        cnt += ans[1] - dd[-1]
        ans = [ans[0], dd[-1]]
        del dd[-1]
        d, l = False, True
    
    else: # l
        cnt += ans[0] - dl[-1]
        ans = [dl[-1], ans[1]]
        del dl[-1]
        l, u = False, True

if cnt == K:
    print(*ans)
else:
    p = cnt - K
    if u: # l에서 끝남
        ans[0] += p
    elif r:
        ans[1] -= p
    elif d:
        ans[0] -= p
    else : # l
        ans[1] += p
    print(*ans)

```

----
제일 빨랐던 코드
```python
C, R = map(int, input().split())
K = int(input())

dx = [ i for i in range(C-1, 0, -1) ] + [C]
dy = [ i for i in range(R-1, 0, -1) ] + [R]
moving = [[0, 1], [1, 0], [0, -1], [-1, 0]]

i , j = 1, R
cnt = R
midx = 0 
u, d, r, l = 1, 0, 0, 0
if K > C*R: # K 값이 범위보다 큰 경우2
    print(0)
    quit()

while cnt < K :
    if moving[midx % 4][0] == 0 :
        j += moving[midx % 4][1] * dy[0]
    else:
        i += moving[midx % 4][0] * dx[0]

    if 1+u <= i <= C-d  and 1+l <= j <= R-r :
        if moving[midx % 4][0] == 0:
            cnt += dy[0]
            del dy[0]
            if midx % 4 == 0 :
                u += 1
            else:
                d += 1
        else:
            cnt += dx[0]
            del dx[0]
            if midx % 4 == 1 :
                r += 1
            else:
                l += 1
    else:
        if moving[midx % 4][0] == 0:
            j -= moving[midx % 4][1] * dy[0]
        else:
            i -= moving[midx % 4][0] * dx[0]
        
        midx += 1
        

if cnt == K:
    print(i, j)
else:
    p = cnt - K
    i -= moving[midx % 4][0] * p
    j -= moving[midx % 4][1] * p
    
    print(i, j)

```