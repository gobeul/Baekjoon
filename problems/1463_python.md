### 백준 1463번 - 1로 만들기

> 2022/08/13 <br>
> 무조건 3으로 나눌수 있도록 하는게 맞는게 같았는데 아니었다.<br>
> 고로 그리드로 접근하기는 힘들었다.<br>
> 다른 분의 풀이를 참고했는데 인덱스 번호를 숫자리스트로 치환(?)해서 접근한는 방법이 꽤나 많은것 같다.

```python
n = int(input())

num = [0]*(n+1)

for i in range(2, n+1):
    num[i] = num[i-1] + 1
    if i % 2 == 0:
        num[i] = min(num[i], num[i//2]+1)
    if i % 3 == 0:
        num[i] = min(num[i], num[i//3]+1)

print(num[n]))
```