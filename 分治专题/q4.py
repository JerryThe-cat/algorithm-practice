import sys

def solve(n):
    # 初始化 n×n 的表格
    table = [[0] * n for _ in range(n)]

    # 基础情况：2×2 的小积木
    table[0][0] = 1
    table[0][1] = 2
    table[1][0] = 2
    table[1][1] = 1

    # 从 m=2 开始，每次翻倍，直到 m=n
    m = 2
    while m < n:
        # 右上角 = 左上角 + m
        for i in range(m):
            for j in range(m):
                table[i][j + m] = table[i][j] + m
                table[i + m][j] = table[i][j] + m
                table[i + m][j + m] = table[i][j]

        m *= 2

    # 输出
    for i in range(n):
        print(' '.join(str(x) for x in table[i]))

for line in sys.stdin:
    line = line.strip()
    if line:
        n = int(line)
        solve(n)
    