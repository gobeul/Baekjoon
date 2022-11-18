### 백준 9251번 - LCS

> 2022/11/18 <br>
> LCS 최장 공통 부분 수열 알고리즘<br>
> 이문제는 블로그글을 참고하였다.<br>
> https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

N, M = len(A), len(B)

arr = [[0]*(M+1) for _ in range((N+1))] # 패딩을 준 배열

for i in range(1, N+1):
    a = A[i-1]
    for j in range(1, M+1):
        b = B[j-1]
        if a == b:
            arr[i][j] = arr[i-1][j-1] + 1 # 같은 경우 
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])


print(arr[N][M])
```