### 백준 19236번 - 청소년 상어

> 2022/10/30 <br>
> 함수에 인자 값으로 배열을 넣어 주면 그 배열을 독립적으로 참조를 안하는 배열이 나오는 줄 알았는데 아니었다. 함수 인자로 글로벌의 배열을 주면 함수내에서 그 배열을 글로벌 배열을 참조 하고 있는 상태 였다.<br>
> 예시<br>
```python
def tmp_function(v):
    v[0] = 1

a = [0,1,2,3,4,5]

print(a) # => [0,1,2,3,4,5]

tmp_function(a)

print(a) # => [1,1,2,3,4,5] # 지역변수의 a의 값을 바꿨는데 글로벌 a의 값도 변했다.
```
> 순열 조합등에서 재귀를 거치며 배열을 건드는 경우가 많은데 이런 부분은 조심해야될것 같다.


```python
import sys
import copy
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline


def recur(si, sj, d, v, arr, alive): # 상어 좌표 / 상어 방향 / 총합 / 배치 /
    global ans
    
    # 1. 물고기 이동
    for fish_num in range(1, 17):
        flag = False
        if not alive[fish_num]:
            continue

        for i in range(4): 
            for j in range(4):
                if arr[i][j] and arr[i][j][0] == fish_num : # False 걸러주기 위해 arr[i][j] 를 추가해준다.
                    fish_dir = arr[i][j][1]
                    while 1:
                        mi, mj = i+delta[fish_dir][0], j+delta[fish_dir][1]

                        if is_range(mi, mj) and arr[mi][mj] != 'shark' :
                            arr[i][j] = (fish_num, fish_dir) # 방향 새로고침 해줌
                            arr[i][j], arr[mi][mj] = arr[mi][mj], arr[i][j]
                            flag = True
                            break
                        fish_dir = (fish_dir+1)%8 # 갈곳이 없어 방향 회전
                        
                if flag:
                    break
            if flag:
                break
    
    # 2. 먹을 수 있는 물고기 확인
    fish_list = possible(si, sj, d, arr) # 먹을 수 있는 물고기
    
    if fish_list == []: # 먹을 수 있는 물고기가 없음
        ans = max(ans, v)
        return 
        
    # 3. 재귀
    for fi, fj in fish_list:
        other_arr = copy.deepcopy(arr) #
        other_alive = alive[:]
        fish_info = other_arr[fi][fj]

        other_arr[fi][fj] = 'shark'
        other_arr[si][sj] = False
        other_alive[fish_info[0]] = False

        recur(fi, fj, fish_info[1], v+fish_info[0], other_arr, other_alive)

        # alive[fish_info[0]] = True
        # arr[si][sj] = 'shark'
        # arr[fi][fj] = fish_info
    

def possible(si, sj, d, arr): # 방향에 있는 먹을 수 있는 물고기들

    fish = []
    di, dj = delta[d][0], delta[d][1]
    for k in range(1, 4):
        mi = si + di*k 
        mj = sj + dj*k
        if is_range(mi, mj) and arr[mi][mj] :
            fish.append((mi,mj))

    return fish

def is_range(i, j):
    if 0 <= i < 4 and 0 <= j < 4 :
        return True
    return False


delta = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)] # 반시계 방향 델타

arr = []
for _ in range(4):
    lst = list(map(int, input().split()))
    tmp = []
    for i in range(0, 8, 2):
        tmp.append((lst[i], lst[i+1]-1)) # 델타 인덱스에 맞추기 위해 -1 해줌
    arr.append(tmp)


shark_d = arr[0][0][1] # 상어 방향 
ans = arr[0][0][0] # 물고기 번호 합
alive = [True]*17 # 살아있는 물고기 들
alive[ans] = False
arr[0][0] = 'shark'

recur(0, 0, shark_d, ans, arr, alive)

print(ans)
```