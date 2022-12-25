"""
step = [
    [],
    [1번 계단을 밟는 경우], # 경우의 수 1개
    [2번 계단을 밟는 경우], # 0->1->2 or 0->2 경우의 수 2개
    [3번 계단을 밟는 경우], # 0->1->3 or 0->2-> 경우의 수 2개
    .
    .
    .
    [N번 계단을 밟는 경우]
]
"""
def FinD(arr): # s가 1인 친구에서 가장 큰 놈, 2인 친구에서 가장 큰놈을 뽑아주자
    one = []
    two = []
    for s, p in arr :
        if s == 1:
            one.append((s,p))
        else:
            two.append((s,p))
    s1, p1 = max(one, key=lambda x : x[1])
    s2, p2 = max(two, key=lambda x : x[1])
    return s1, p1, s2, p2

N = int(input())
point = [0 for _ in range(N+2)] # 계단 점수, N-1 에서 N+1 로 갈 경우에 대비해 크기여유

for i in range(1, N+1): # 1번 부터 N번까지의 점수입력
    point[i] = int(input())

step = [[] for _ in range(N+2)] # (0,0) = 연속 포인트? , 계단점수
step[1].append((1,point[1]))
step[1].append((2,0)) # 더미용 FinD 에서 오류 없애기 위해
step[2].append((1,point[2]))
step[2].append((2,point[1]+point[2]))

for i in range(1, N): # 1번 부터 N-1 까지
    s1, p1, s2, p2 = FinD(step[i]) # i 번째에서 최대깂들을 뽑는다.
    # 1칸 점프 => s += 1 이고 s가 2 이면 1칸 점프 할 수 없음. (s1 만 됨)
    step[i+1].append((s1+1, p1+point[i+1]))
    # 2칸 점프 => s = 1 (s1, s2 다됨)
    step[i+2].append((1, p1+point[i+2]))
    step[i+2].append((1, p2+point[i+2]))


# N-1 번 계단에서 가장 큰 값이 있을 수 있음.
a = max(step[N], key=lambda x : x[1])[1]
# b = max(step[N-1], key=lambda x : x[1])[1]
print(max(a))