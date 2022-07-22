### 백준 2309번 - 일곱 난쟁이

> 2022/07/22 <br>


```python
from collections import deque

total_list = deque([])

for i in range(9): # 주어진 9난쟁이 리스트에 모두 저장.
    total_list.append(int(input()))

double_for = True # 2중 for 문 탈출용 라벨
for i in range(9):
    l = total_list.popleft() # 맨 왼쪽 빼서 8명 만들기
    total_sum = sum(total_list) # 8명 합
    for j in range(8): # 8명에서 하나씩 빼보기
        if total_sum - total_list[j] == 100:
            del total_list[j]
            double_for = False
            break
    
    if double_for == False:
        break
    total_list.append(l) # l 이 맞으면 다시 오른쪽에 추가

total_list = list(total_list) # sort() 사용을 위해 다시 리스트로 만들기
total_list.sort()

for i in total_list: 
    print(i)
```