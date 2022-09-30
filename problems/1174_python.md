### 백준 1174번 - 줄어드는 수

> 2022/09/30 <br>
> 줄어드는 수의 규칙을 찾고 이를 바탕으로 구현했다.<br>
>
> 코드의 가독성이 떨어지는 건 아쉽지만 실행시간은 주어진 시간에 비해 작게 나와서 만족한다.
```python
"""
n자리 숫자에서 나올 수 있는 경우의 수
n = 1 (앞자리 0부터) -> [1,1,1,1,1,1,1,1,1,1]
n = 2 (앞자리 1부터) -> [0,1,2,3,4,5,6,7,8,9]
n = 3 (앞자리 2부터) -> [0,0,1,3,6,10,15,21,28,36]
n = 4 (앞자리 3부터) -> [0,0,0,1,4,10,20,35,56,84]
....
n = 10 (앞자리 9부터) -> [0,0,0,0,0,0,0,0,0,1]

1. N번째 작은 수가 몇의 자리의 숫자인지 파악.
2. m 자리의 가장 작은 줄어드는 수부터 1개씩 올려가며 찾는다.
"""

def howlong(lst, m, a): # lst 는 m자리 숫자에서의 맨앞자리의 숫자에 따른 경우의 수, a는 누적된 경우의수(0부터 시작)
    global jj

    if m > 10: # 작은 수는 딱 10자리의 정수까지만 만들 수 있다. 9876543210 -> 최대 값
        return
    if m > 1 : # m자리의 따른 lst 만들기. m == 1은 기본 basic 사용
        tmp = [0]*10 # m자리의 정보가 들어갈 임시리스트
        for i in range(m-1, 10): # m자리의 숫자가 될 수 있는 줄어드는 수는 맨앞자리가 m-1부터 시작이다. 즉 m-1 밑으로는 lst 인덱스값이 0(없다)이다.
            tmp[i] = sum(lst[:i]) # m자리의 앞자리가 x인 경우의 수는 m-1자리의 앞자리가 0 ~ x-1 까지의 모든 경우의 수를 합한것과 같다.
        lst = tmp
    if N <= a+sum(lst): # m 자리의 까지의 모든 경우의 수보다 작다면 N번째 작은 수는 m 자리의 숫자이다.
        jj = [m, a]  # N번째 줄어드는 수는 m자리의 처음부터 N-a 번째 숫자이다.
        return
    else:
        howlong(lst, m+1, a+sum(lst)) # 범위이상이면 다음 자리로.

def find_number(m, a, cnt, number):
    if cnt == 1: # m자리의 숫자에서 가장 작은 수
        number = ""
        for i in range(m-1, -1, -1):
            number += str(i)

    if N - a == cnt:
        print(number)
        return

    number = make_number(number)

    find_number(m, a, cnt+1, number)
    

def make_number(number): # number 다음의 줄어드는 수 만들기.
    pointer = len(number)-1
    if pointer == 0: # number 가 1자리 숫자라면
        k = int(number)+1
        return str(k)

    while pointer > 0:
        if int(number[pointer]) +1 == int(number[pointer-1]): # 
            pointer -= 1 # 포인터 왼쪽 전진
        else:
            break

    ans = ""
    # pointer 기준으로..
    ans += number[:pointer] # 포인터 이전까지는 그래로 붙이기.
    ans += str(int(number[pointer])+1) # 포인터 위치 1증가 시켜서 붙이기
    # 뒤에 값들 초기화해서 붙이기
    cnt = len(number) - len(ans) # 모자란 길이
    for i in range(cnt-1, -1, -1): # 모자란 길이가 3이면 210 이 붙을 것이고, 5면 43210 이 붙을 것이다.
        ans += str(i)
            
    return ans

N = int(input())
basic = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 기본 1자리 숫자일때 맨앞자리에 숫자 n(index)이 오는 경우 가질 수 있는 경우의 수
jj = [-1, -1]
howlong(basic, 1, 0) # 1자리의 수 / 누적범위 : ~10 부터 시작

if jj == [-1, -1]:
    print(-1) # 넘어간 범위
else:
    find_number(jj[0], jj[1], 1, "")
```