### 백준 2477번 - 참외밭

> 2022/07/22 <br>
> 방향숫자를 이용하여 주저진 모양이 어떤 모양인지 찾은 후 직사각형 넓이에서 비어있는 직사각형 넓이를 빼는 방법으로 접근하였다.<br>
> (4 가지 모양 모두 큰 넓이와 작은 넓이는 만드는 방향순서쌍이 다르기 때문)


```python
n = int(input())

angle_shape = 0
way = []
for i in range(6):
    a, b = map(int, input().split())
    way.append([b, a])
    # 동쪽이 1 인경우 'ㄴ' 과 '역 ㄱ' 의 방향숫자합이 같았다. 그래서 변화를 주었다.
    if a == 1:
        a = 10 
    angle_shape += a

big_area = 0
small_area = 0

#for-else 문은 for 문이 온전히 break 없이 실행되면 eles 문이 실행된다. 
if angle_shape == 32: # ㄱ 모양
    for i in range(5):
        if way[i][1] == 1 and way[i+1][1] == 3:
            small_area = way[i][0] * way[i+1][0]
            break
    else:
        small_area = way[0][0] * way[-1][0]

    for i in range(5):
        if way[i][1] == 4 and way[i+1][1] == 2:
            big_area = way[i][0] * way[i+1][0]
            break
    else:
        big_area = way[0][0] * way[-1][0]

elif angle_shape == 25: # ㄴ 모양
    for i in range(5):
        if way[i][1] == 2 and way[i+1][1] == 4:
            small_area = way[i][0] * way[i+1][0]
            break
    else:
        small_area = way[0][0] * way[-1][0]

    for i in range(5):
        if way[i][1] == 3 and way[i+1][1] == 1:
            big_area = way[i][0] * way[i+1][0]
            break
    else:
        big_area = way[0][0] * way[-1][0]

elif angle_shape == 24: # 역, ㄴ 모양
    for i in range(5):
        if way[i][1] == 3 and way[i+1][1] == 2:
            small_area = way[i][0] * way[i+1][0]
            break
    else:
        small_area = way[0][0] * way[-1][0]

    for i in range(5):
        if way[i][1] == 1 and way[i+1][1] == 4:
            big_area = way[i][0] * way[i+1][0]
            break
    else:
        big_area = way[0][0] * way[-1][0]

else: # 33 역, ㄱ 모양
    for i in range(5):
        if way[i][1] == 4 and way[i+1][1] == 1:
            small_area = way[i][0] * way[i+1][0]
            break
    else:
        small_area = way[0][0] * way[-1][0]

    for i in range(5):
        if way[i][1] == 2 and way[i+1][1] == 3:
            big_area = way[i][0] * way[i+1][0]
            break
    else:
        big_area = way[0][0] * way[-1][0]


print(n*(big_area - small_area))
```
