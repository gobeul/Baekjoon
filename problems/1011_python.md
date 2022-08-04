### 백준 1011번 - Fly me to the Alpha Centauri

> 2022/08/04 <br>
> 풀이는 밑에 사진 참고!

```python
def half(k):
    for i in range(2**16): # 범위 k로 해도 될듯
        if k <= i*(i+1): # ( i*(i+1)/2 ) * 2 == 2*p
            return i, i*(i+1)/2, i*(i-1)/2 # d, p, q

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    t = y - x
    d, p, q = half(t)

    if p + q < t :
        print(2*d)
    else : # t <= p + q
        print(2*d -1)
```

![1011_1](Baekjoon/1011_1.jpg)

![1011_2](Baekjoon/1011_2.jpg)