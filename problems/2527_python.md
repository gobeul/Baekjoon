### 백준 2527번 - 직사각형

> 2022/07/25 <br>
> 테스트 케이스 통과 + 시간줄이기 에서 상당히 시간을 많이 쓴 문제였다.<br>
> 선분에있는 좌표점을 모두 모아서 하는 방법을 생각해 봤는데 시간초과로 실패했고,<br>
> 그리고 나서 생각한것이 왼쪽 사각형을 기준으로 잡고 경우의 수에 해당하는 좌표 범위를 설정하는 방법이다. 이 방법으로 코드의 길이도 꽤 줄일 수 있었고 시간적인 부분도 획기적으로 개선했다.

```python
for t in range(4):

    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    sq_1 = [[p1, q1], [x1, q1], [x1, y1], [p1, y1]]
    sq_2 = [[p2, q2], [x2, q2], [x2, y2], [p2, y2]]

    aa =True

    if x1 < x2 :  ## 왼쪽 직사각형을 선정하는 부분
        left_sq = sq_1
        right_sq = sq_2
    elif x1 > x2 :
        left_sq = sq_2
        right_sq = sq_1
    else: ####### x1 == x2
        aa = False
        if y1 > q2 or y2 > q1: 
            print("d")
        elif y1 == q2 or y2 == q1:
            print("b")
        else:
            print("a")

    while aa:
        if left_sq[0][1] < right_sq[2][1] or left_sq[0][0] < right_sq[1][0] or left_sq[3][1] > right_sq[0][1] :
            print("d") 
        elif left_sq[0] == right_sq[2] or left_sq[3] == right_sq[1]:
            print("c")
        elif left_sq[0][1] == right_sq[3][1] or left_sq[0][0] == right_sq[1][0] or left_sq[3][1] == right_sq[0][1]:
            print("b")
        else:
            print("a")
        break
```