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

![1011_1](https://user-images.githubusercontent.com/109266805/182877357-bc4cad03-1297-48f8-b03c-99a606a9d5bb.jpg)

![1011_2](https://user-images.githubusercontent.com/109266805/182877507-a548492a-af10-4633-8825-3fafdca7a9e1.jpg)