### 백준 1043번 - 거짓말

> 2022/09/16 <br>
> 문제를 잘못이해 해서 한번 엎었지만 문제만 잘 이해하면 쉬운 문제 같다. 왜 골드 난이도인지 모를정도

```python
def Done(): # 더 이상 갈 수 있는 파티가 없다면 True 를 반환
    for i in check_party:
        if i:
            return False
    return True

def areyouknow(party_info): # 진실을 아는 자가 파티에 있는지
    for i in party_info:
        if visited[i]:
            return True
    return False

def visit(lst): # 방문처리(진실을 알려줌)
    for i in lst:
        visited[i] = True


N, M = map(int, input().split()) # N 사람수, M 파티 수
visited = [False]*(N+1) # 사람번호는 1부터
visited[0] = True

kn, *knower = map(int, input().split())
visit(knower)

total_party = []
for _ in range(M):
    party_num, *join = map(int, input().split())
    total_party.append((party_num, join))

check_party = [True]*M # 거짓말 할수 있는 가능성이 있는 파티

re = True
while re:
    re = False
    ans = 0
    if Done(): 
        break

    for party_num, lst in enumerate(total_party):
        if check_party[party_num] and areyouknow(lst[1]):
            visit(lst[1]) # 있으면 진실을 아는자의 모임에 껴줌
            check_party[party_num] = False # 그리고 이 파티는 더 이상 고려 안함
            re = True
        elif check_party[party_num]:
            ans += 1

print(ans)
```