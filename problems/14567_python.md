### 백준 14503번 - 선수과목 (Prerequisite)

> 2022/12/11 <br>
> defaultdict을 사용해서 선수과목의 정보를 딕셔너리에 저장후 판단하는 방법으로 풀이했다.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split()) # N 과목 수 // M 조건 수

# 과목들의 수강 여부 와 학기
subject = [(True, 1) for _ in range(N+1)] 

# 선수 과목 조건들
# key 수강 과목 번호, value 들어야하는 과목들
pre = defaultdict(list)
for i in range(M):
    # b 를 듣기 위해 a를 들어야 한다.
    a, b = map(int, input().split())
    pre[b].append(a)

    subject[b] = (False,1) # b 는 바로 들을 수 없음

flag = True
while flag:
    flag = False # 다 수강했음
    # s 수강과목 // p 선수과목들
    for s, p in pre.items():
        if subject[s][0]:
            continue # 이미 수강했으면 pass
        v = subject[s][1]
        for _ in range(len(pre[s])): # 선수과목 수 만큼
            k = pre[s].pop() # 선수과목 k
            if subject[k][0]: # 수강되어 있으면
                v = max(subject[k][1]+1, v) # 몇학기에 들을 수 있는가
            else: # 수강 안했으면
                pre[s].append(k) # 다시 리스트에 넣고
                flag = True # while문 다시 돌아야 됨
                subject[s] = (False, v) # v 값 갱신
                break
        else:
            subject[s] = (True, v) # break 를 안받았다면 수강할 수 있음

for i in range(1, N+1):
    print(subject[i][1], end=' ')
print()

```