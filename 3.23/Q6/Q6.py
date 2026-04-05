import sys

def division(n, m):
    # 终止条件
    if n == 1 or m == 1:
        return 1
    if n == m:
        return division(n, m -1) + 1
    if n < m:
        return division(n, n)
    
    # 递归调用
    return division(n, m - 1) + division(n - m, m)


for line in sys.stdin:
    n = int(line.strip())
    print(division(n, n))