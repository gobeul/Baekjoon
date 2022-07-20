### 백준 1244번 - 스위치 켜고 끄기

> 2022/07/20 <br>


```python
sw_n = int(input())
sw_situation = list(map(int, input().split()))

p_n = int(input()) 
for t in range(p_n):
    gender, num = map(int, input().split())
    if gender == 1:
        for i, s in enumerate(sw_situation, start=1):
            if i%num == 0:
                if s: #스위치 상태 바꾸기
                    sw_situation[i-1] = 0
                else:
                    sw_situation[i-1] = 1
    else:
        pos = 1 # 대칭 크기
        num -= 1 # 인덱스랑 맞춰주기
        if num == 0: # 여자가 1번을 받는 경우
            if sw_situation[0]:
                sw_situation[0] = 0
            else:
                sw_situation[0] = 1
        elif num == sw_n-1: # 여자가 마지막 번호를 받는 경우
            if sw_situation[-1]:
                sw_situation[-1] = 0
            else:
                sw_situation[-1] = 1
        else:
            while 1: # 대칭 범위 찾기
                if (num - pos >= 0) and (num + pos < sw_n):
                    if sw_situation[num - pos] == sw_situation[num + pos]:
                        pos += 1
                    else:
                        pos -= 1
                        break
                else:
                    pos -=1
                    break
            for i in range(num-pos, num+pos+1): # 대칭 만큼 스위치 바꾸기
                if sw_situation[i]:
                    sw_situation[i] = 0
                else:
                    sw_situation[i] = 1


for i, s in enumerate(sw_situation): # 20*n + 1 번째 스위치마다 줄바꿔서 출력
    if (i > 0) and (i % 20) == 0:
        print("\n", end="")
    print(s, end=" ")
```