### 백준 20437번 -문자열 게임 2

> 2022/10/28 <br>
>  python3 시간초과 // pypy 통과<br>
> 다른 분 풀이의 빠른 코드를 보니 딕셔너리에 해당 문자의 인덱스를 리스트로 저장하여 그 인덱스를 이용하여 바로 문자열 길이를 계산하는 방법으로 시간을 효율적으로 줄였다.


```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

cc = int(input())
for _ in range(cc):
    word = list(input())
    K = int(input())

    dict = {} # 문자수 카운팅하기
    for w in word:
        try:
            dict[w] += 1
        except:
            dict[w] = 1

    N = len(word)
    max_len, min_len = 0, N

    for i, s in enumerate(word):
        if dict[s] < K:
            continue
        
        dict[s] -= 1
        cnt = 1 # 특정 문자가 포함 된 개수
        j = i+1
        length = 1 # 문자열 길이
        while cnt < K and j < N:
            if word[j] == s:
                cnt += 1

            length += 1
            j += 1
        
        max_len = max(max_len, length)
        min_len = min(min_len, length)

    if max_len == 0 : # 없는 경우
        print(-1)
    else:
        print(min_len, max_len)
```