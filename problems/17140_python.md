### 백준 17140번 - 이차원 배열과 연산

> 2022/10/22 <br>
> zip 를 이용한 2차원 배열 회전으로 문제를 풀 수 있었다.<br>
> 한가지 알게 된점은 zip을 이용한 배열 회전이 한 방향을 기준으로 90도 회전인줄알았는데 아니었다..<br>
> zip을 이용해서 배열을 2번 회전시키면 원래대로 돌아온다..!<br>


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

"""
zip 을 이용해서 배열을 두번 회전하면 원래대로 돌아옴
"""

def numbersort(lst):
    dict = {}
    for i in lst:
        if i: # 0 은 무시
            try:
                dict[i] += 1
            except:
                dict[i] = 1
    
    tmp = []
    for num, cnt in dict.items():
        tmp.append((num, cnt))
    tmp.sort(key=lambda x : (x[1], x[0])) # 튜플 형식

    tmp2 = []
    for a, b in tmp:
        tmp2.append(a)
        tmp2.append(b)

    return tmp2[:100] # 100 개까지


def Msort(w): # 가로 정렬
    global tm


    tm = 0 # 정렬된 가로 길이
    for i in range(w): # 행 개수 만큼 반복
        arr[i] = numbersort(arr[i])
        tm = max(tm, len(arr[i]))
        
    for i in range(w): # 0 채우기
        k = len(arr[i])
        arr[i] += [0]*(tm-k)


ei, ej, x = map(int, input().split())

arr = [list(map(int, input().split()))  for _ in range(3)]
N, M = 3, 3

time = 0
while time <= 100:
    try:
        if arr[ei-1][ej-1] == x:
            break
    except:
        pass
    
    if N >= M : # R 연산
        Msort(N)
        M = tm
    
    else: # R연산
        arr = list(map(list, zip(*arr)))
        Msort(M)
        arr = list(map(list, zip(*arr)))
        N = tm
    
    time += 1

if time > 100:
    print(-1)
else:
    print(time)
```