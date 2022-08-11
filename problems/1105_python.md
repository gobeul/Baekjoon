### 백준 1105번 - 팔

> 2022/08/11 <br>
> 그리드 알고리즘 - 가능한 경우를 따져가며 "0"의 출력을 목표로 생각했다.

```python
def c8(n): # 숫자 8을 세는 함수
    a = list(str(n))
    c = 0
    for i in a:
        if i == "8":
            c += 1
    return c

def e_c(arr1, arr2): # 자리수와 맨 앞자리가 같을경우 
    cnt = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i] == "8":
            cnt +=1
        elif arr1[i] == arr2[i] :
            pass
        else:
            return cnt
    return cnt

N, M = map(int, input().split())
n_list = list(str(N))
m_list = list(str(M))

if len(n_list) != len(m_list) : # 자리수가 다를경우 무조권 0, 9가 있기 때문에 "0"
    print(0)

else: # 자리수가 같을경우

    if n_list[0] == m_list[0] : # 앞자리가 같을경우
        print(e_c(n_list, m_list)) # 둘중 8이 작은 값
        # 앞자리부터 8이 같은 경우만 보기 중간에 끝기면 끝
        ## 예 8808 8888 인경우 앞에 88만 유효해서 2를 반환
        ### 8808 8808 은 0은 카운트를 안해서 3을 반환

    else: # 앞자리가 다를 경우, 얘도 9가 있어서 무조건 0
        print(0)

```