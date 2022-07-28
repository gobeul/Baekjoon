### 백준 2564번 - 경비원

> 2022/07/28 <br>
> 내위치의 방향에 따라 계산방법을 고정시킬 수 있어서 4가지 경우의 수를 모두 구해 풀었다.

```python
W, H = map(int, input().split())

N = int(input())
# 북 1[0] // 남 2[1] // 서 3[2] // 동 4[3]
square = [[], [], [], []]
for i in range(N):
    s_dir, s_pos = map(int, input().split())
    square[s_dir -1].append(s_pos) # 상점들 칸 수 
m_dir, m_pos = map(int, input().split())

r_s_dir = [] # 내 맞은편 상점들의 기준점 반대 방향 칸 수 
ans = 0

if m_dir == 2 : # 남쪽, 리버스는 북쪽
    r_m_pos = W - m_pos # 내 기준점 반대 방향 칸수
    for i, v in enumerate(square[0]): # 맞은편 방향
        r_s_dir.append(W-v)
        ans += min(r_s_dir[i]+r_m_pos, v+m_pos) + H
    for i in square[1]: # 같은 방향
        ans += abs(m_pos - i)
    for i in square[2]:
        ans += H - i + m_pos
    for i in square[3]:
        ans += H - i + r_m_pos

elif m_dir == 1 : # 북쪽
    r_m_pos = W - m_pos
    for i in square[0]:
        ans += abs(m_pos - i)
    for i, v in enumerate(square[1]):
        r_s_dir.append(W-v)
        ans += min(r_s_dir[i]+r_m_pos, v+m_pos) + H
    for i in square[2]:
        ans += i + m_pos
    for i in square[3]:
        ans += i + r_m_pos

elif m_dir == 3 : # 서
    r_m_pos = H - m_pos
    for i in square[0]:
        ans += i + m_pos
    for i in square[1]:
        ans += i + r_m_pos
    for i in square[2]:
        ans += abs(m_pos - i)
    for i, v in enumerate(square[3]):
        r_s_dir.append(H-v)
        ans += min(r_s_dir[i]+r_m_pos, v+m_pos) + W

else: # 동
    r_m_pos = H - m_pos
    for i in square[0]:
        ans += W - i + m_pos
    for i in square[1]:
        ans += W - i + r_m_pos
    for i, v in enumerate(square[2]):
        r_s_dir.append(H-v)
        ans += min(r_s_dir[i]+r_m_pos, v+m_pos) + W
    for i in square[3]:
        ans += abs(m_pos - i)

print(ans)
```