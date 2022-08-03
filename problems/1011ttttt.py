def half(k):
    for i in range(2**16): # 범위 k로 해도 될긋??
        if k < i*(i+1)/2:
            return (i-1), i*(i-1)/2

import math

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if y-x == 1:
        print(1)
    else:
        p = math.ceil((y-x)/2)
        d, k = half(p)

        if k == p:
            print(2*d)
        else:
            print(2*d +1)
