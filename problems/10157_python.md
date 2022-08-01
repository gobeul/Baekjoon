### 백준 10157번 - 자리배정

> 2022/07/31 <br>
> 동서남북 이동에 있어 그방향의 이동이 끝나는 좌표의값을 이용하여 방향을 구분짓고 계산했다.

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