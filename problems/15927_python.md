### 백준 15927번 - 회문은 회문아니야!!

> 2022/11/05 <br>
> 길이 S 인 문자열이 회문이라면 S-1만큼 문자열(K)을 봤을때,<br>
> K 가 회문이라면 그 문자열은 1가지 문자로만 이루어진 회문이다.<br>
> 회문이 아니라면 그대로 가장 긴 회문은 S-1 길이가 되는 것.

```python
import sys
sys.stdin = open('ee.txt', 'r')
input = sys.stdin.readline

def check(j):
    global b
    for i in range(b, j):
        if word[i] != word[j-i]:
            b = i
            return False # 펠린드롬 아님
    b = j-1
    return True # 펠린드롬임

word = input().rstrip()
j = 1
b = 0
ans = -1
k = word[0]
while j < len(word):
    if k == word[j] and check(j):
        pass
    else:
        ans = j+1

    j += 1

print(ans)
```