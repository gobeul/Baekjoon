import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
r_num = num.copy()

ans = 2
cnt = 0
while len(num) > ans:
    if num[cnt] <= num[cnt+1] :
        cnt += 1
        if cnt + 1 > ans :
            ans = cnt + 1
    else:
        del num[:cnt+1]
        cnt = 0 

cnt = 0
while len(r_num) > ans:
    if r_num[cnt] >= r_num[cnt+1] :
        cnt += 1
        if cnt + 1 > ans :
            ans = cnt + 1
    else:
        del r_num[:cnt+1]
        cnt = 0

if n == 1:
    ans = 1
    
print(ans)