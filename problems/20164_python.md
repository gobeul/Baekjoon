### 백준 20164번 - 홀수 홀릭 호석

> 2022/12/07 <br>
> 세자리 수 이상일 경우에 이중 for 문으로 자를 위치를 선정하여 해결했다. 어렵지 않았던 문제<br>


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

# 홀수 개수 카운트
def odd_cnt(num): # 숫자(str)
    v = 0
    for i in num:
        v += int(i)%2
    return v

def recur(num, cnt): # 숫자(str) / 홀수 개수(누적)
    global max_ans, min_ans

    cnt += odd_cnt(num)
    n = len(num)
    if n == 1:
        max_ans = max(max_ans, cnt)
        min_ans = min(min_ans, cnt)
        return
    
    if n == 2:
        new_num = str(int(num[0]) + int(num[1]))
        recur(new_num, cnt)
        return 
    
    if n >= 3:
        for a in range(1, n-1):
            for b in range(a+1, n):
                first = int(num[:a]) # 첫번째 숫자
                second = int(num[a:b]) # 두번째 숫자
                third = int(num[b:]) # 세번째 숫자
                new_num = str(first + second + third)
                recur(new_num, cnt)


N = input().rstrip()
max_ans = -1
min_ans = 99999999

recur(N, 0)

print(min_ans, max_ans)     
```