import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

ans_deq = deque(num_list[:k])
ans = sum(ans_deq)
del num_list[:k]

num_list = deque(num_list)

while num_list:
    l_v = num_list.popleft()
    wast = ans_deq.popleft()

    ans_deq.append(l_v)
    s = sum(ans_deq)

    if s > ans:
        ans = s

print(ans)
        

    