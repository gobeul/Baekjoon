### 백준 1052번 - 물병

> 2022/08/07 <br>
> 물병에 들어있을 수 있는 물의 양은 1, 2, 4, 8, 16 ... 순이다<br>
> 모든 물병의속 물이 같을 필요는 없으므로 2진수의 표현법으로 정리할 수 있다.

```python
n, k = map(int, input().split())

ans = 0
while bin(n).count("1") > k:
    n += 1 # 물의 양이 1l 씩 증가.
    ans += 1

print(ans)
```