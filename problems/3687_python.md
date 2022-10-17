### 백준 3687번 - 성냥개비

> 2022/10/17 <br>
> 조합을 모두 찾으면 당연하게도 시간초과다. -> 큰수는 최대한 많은 자릿수를 받아야 하기에 작은 수(2) 부터 채워나가면 되고 , 작은 수는 자릿수를 최대한 줄여야 하기에 큰 수부터 채워나가는 방법으로 시간 초과를 피할 수 있었다.<br>
>
> 같은 자리수에 대해서는 큰수의 경우 2, 3 이 아니면 4부터는 2+2 조합이 더 커지기에 고려할 필요가 없었고 작은 수의 경우만 같은 자리수에 대해 비교를 해주었다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline


def recur_max(s, lst, last): # 성냥개비 총 개수로 조합가능한 경우 찾기 _ 숫자 최대
    global max_lst, max_flag
    if s > N or max_flag:
        return

    if s == N: # 맨처음 찍히는게 숫자 최대값
        max_lst = lst
        max_flag = True
        return
    
    for i in range(last, 6):
        a = matchstick[i]
        recur_max(s+a, lst+[a], i)

def recur_min(s, lst, last, cnt): # 성냥개비 총 개수로 조합가능한 경우 찾기 _ 숫자 최대
    global min_lst, min_flag, min_cnt
    if s > N or (min_flag and min_cnt < cnt):
        return

    if s == N: # 맨처음 찍히는게 숫자 최소겂
        min_lst.append(lst)
        min_flag = True
        min_cnt = cnt
        return

    for i in range(last, -1, -1):
        a = matchstick[i]
        recur_min(s+a, lst+[a], i, cnt+1)


def trans_number_max(lst): # lst 안에 성냥 개비 개수들을 최대 숫자로 변환
    k = []
    for i in lst:
        k.append(dict_max[i])
    
    v = make_max(k)
    return v

def trans_number_min(lst):
    k = []
    for i in lst:
        k.append(dict_min[i])
    
    v = make_min(k)
    return v    

def make_max(lst): # 최대값 만들기
    lst.sort(reverse = True) # 내림 차순 정렬후 그냥 붙이기
    s = ""
    for i in lst:
        s += i
    return int(s)

def make_min(lst): # 최소값 만들기
    lst.sort() # 오름차순 정렬뒤 0을 고려해줘야함
    s = ""
    for i in lst:
        s += i
    
    if int(s) == 0: # 0 일경우 맨 앞을 '6'으로 바꿔준다
        s = '6'+s[1:]
    
    elif s[0] == '0': # 0은 아닌데 앞자리가 0 일경우
        zero = s.count('0') # 0 개수 카운트
        if int(s[zero]) > 6 : # 처음 나오는 0이 아닌 수가 6보다 클경우 600..00xxx 가 작은수
            s = '6'+'0'*(zero-1)+s[zero:]
        else: # 처음 나오는 0이 아닌수가 6보다 작은 경우 x00..00yyy 가 작은수
            s = s[zero] + '0'*zero + s[zero+1:] # 0들을 그담으로 작은 수 뒤에 다 붙여줌
    return int(s)


# dict = {
#     2 : [1],
#     3 : [7],
#     4 : [4],
#     5 : [2, 3, 5],
#     6 : [0, 6, 9],
#     7 : [8],
# }

dict_max = {
    2 : '1',
    3 : '7',
    4 : '4',
    5 : '5',
    6 : '9',
    7 : '8',
}

dict_min = {
    2 : '1',
    3 : '7',
    4 : '4',
    5 : '2',
    6 : '0', # 6 이 있을 경우 맨 앞자리가 0으로 시작되기 때문에 처리를 해줘야함
    7 : '8',
}

matchstick = [2, 3, 4, 5, 6, 7]  # 숫자가 될 수 있는 성냥개비 수

cc = int(input())
for _ in range(cc):
    N = int(input())

    max_cnt = 0
    max_flag = False
    max_lst = [] # 자리수가 가장 많다면 최대값이 만들어 질 것

    min_cnt = 9999999
    min_flag = False
    min_lst = [] # 자리수가 가장 적다면 최소값이 만들어 질 것(0으로 시작할 수 없으니)

    recur_max(0, [], 0)
    recur_min(0, [], 5, 0)


    ans_min = sys.maxsize
    for i in min_lst: # 최소값 찾기
        ans_min = min(trans_number_min(i), ans_min)


    print(ans_min, trans_number_max(max_lst))
```