### 백준 1991번 - 트리 순회

> 2022/09/13 <br>
> 트리 학습 기념(?) 전위, 중위, 후위 순회 복습

```python
def preorder(a):
    print(a, end="")
    if tree[a][0] != ".":
        preorder(tree[a][0])
    if tree[a][1] != ".":
        preorder(tree[a][1])

def inorder(a):
    if tree[a][0] != ".":
        inorder(tree[a][0])
    print(a, end="")
    if tree[a][1] != ".":
        inorder(tree[a][1])

def posteorder(a):
    if tree[a][0] != ".":
        posteorder(tree[a][0])
    if tree[a][1] != ".":
        posteorder(tree[a][1])
    print(a, end="")

tree = {}

N = int(input())
for _ in range(N):
    p, cl, cr = input().split()
    tree[p] = (cl, cr,)

preorder("A")
print()

inorder("A")
print()

posteorder("A")
print()
```