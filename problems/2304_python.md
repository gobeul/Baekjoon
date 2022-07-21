### 백준 2304번 - 창고 다각형

> 2022/07/22 <br>


```python
N = int(input())
total_list = [list(map(int, input().split())) for i in range(N)]

total_list.sort()
left_0 = total_list[0][0]
right_0 = total_list[-1][0]

total_list.sort(key= lambda x: (x[1], x[0]))

max = total_list.pop(-1)
max_list = [max]

area = max[1] * (right_0 - left_0 +1)


while len(total_list) != 0:
    if total_list[-1][1] == max[1]:
        k = total_list.pop(-1)
        max_list.append(k)

    else:
        break

left_s = max_list[-1][0]
right_s = max_list[0][0]
left_m = max[1]
right_m = max[1]

while left_s != left_0 or right_s != right_0:
    max = total_list.pop(-1)

    if max[0] < left_s:
        area -= (left_s - max[0])*(left_m - max[1])
        left_s = max[0]
        left_m - max[1]

    elif max[0] > right_s:
        area -= (max[0] - right_s)*(right_m - max[1])
        right_s = max[0]
        right_m - max[1]
    
print(area)
```