### 백준 1107번 - 리모컨

> 2022/09/09 <br>
> 처음에는 부르트포스가 아닌 범위를 타이트하게 잡아 풀고 싶었는데 자꾸 반례가 끊임 없이 나와 포기했다..!<br>
> 덕분에 시간은 엄청 오래 잡아먹는다. 3468ms..

```python
def combi(num, s): # num 은 자리수로 0부터 시작, s애는 조합된 번호가 들어갈거임 "" 빈 문자열로 시작
    if num == 2 and int(s) != 0 and int(s[-1]) in broken:  # 이거는 늘어난 자리수 때문에 0이 고장났는데 10xxxxx 이렇게 출력되는거 막을려고
        return

    if num == size:
        if int(s) == 0 and 0 in broken:
            return
        all_combi.append(int(s))
        return

    for i in num_list[num]:
        i = str(i)
        combi(num+1, s+i)

N = input() # 문자열로 받음(인덱스 접근)
k = int(input())

if k == 0: # 고장난 버튼이 없을 경우
    print(min(len(N), abs(100 - int(N))))
    quit()

elif k == 10 : # 모두 고장난 경우
    print(abs(int(N)-100))
    quit()

broken = list(map(int, input().split()))

size = len(N)

num_list = [[] for _ in range(size)] # 각자리에 올 수 있는 번호 리스트

none_broken = []
for i in range(10):
    if i not in broken:
        none_broken.append(i)

for i in num_list:
    i += none_broken

# 자리수가 넘어가는게 더 빠른 경우 일 수 있다.
add = [[0]] # num_list 에 맞춰 2중배열로
for i in range(1, 10):
    if i not in broken:
        add[0].append(i)

size += 1 # 자리수 하나 추가
num_list = add + num_list # 맨 앞자리에 추가.

## 혹은 자리수가 하나 줄어드는게 더 빠를수 있다 == 1번 인덱스에 0 추가
num_list[1].append(0)

# num_list 를 가지고 나올 수 있는 모든 번호 조합 만들기.
## N 의 최대값은 500000 으로 6자리이다. 그러므로 최대 경우의 수는 3^6 = 729 가지의 불과 함! 
all_combi = []
combi(0, "")

ans = 500000 # 버튼 누르는 최소값
N = int(N) # 정수값으로 바꿔주고

for i in all_combi:
    k = min(abs(i - N) + len(str(i)), abs(N - 100)) # 100 에서 출밯하는 거랑 비교해서 넣기

    if k < ans:
        ans = k

print(ans)
```