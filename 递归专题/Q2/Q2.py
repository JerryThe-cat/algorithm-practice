# 基于找规律的程序，但是没什么道理，也不太对
'''from collections import Counter

n = int(input())
sides = n - 1
parents = []
for i in range(sides):
    a,b = map(int, input().split())
    if a == b:
        exit()
    parents.append(a)
n = n - (len(parents) - len(Counter(parents)))
print(n)'''

# 递归：树的深度 = max(左子树深度, 右子树深度) + 1
# 终止条件：节点没有子节点（叶子），深度为1
# 递归调用：求左子树深度和右子树深度
# 返回值：max(左, 右) + 1

n = int(input())
children = {}
parents = {}

for _ in range(n - 1):
    a, b = map(int, input().split())
    children[a] = children.get(a, []) + [b]  # a的子节点
    parents[b] = a                             # b的父节点

# 找根节点（没有父节点的节点）
root = [i for i in range(1, n + 1) if i not in parents][0]

def depth(node):
    # 终止条件：叶子节点
    if node not in children:
        return 1
    
    # 递归求左右子树深度
    max_d = 0
    for child in children[node]:
        max_d = max(max_d, depth(child))
    
    # 返回最大深度 + 1
    return max_d + 1

print(depth(root))
