import sys

def dp(n, m):
    if n == 1 or m == 1:
        return 1
    if n < m:
        return dp(n, n)
    if n == m:
        return dp(n ,m - 1) + 1
    if n > m:
        return dp(n - m, m) + dp(n, m - 1)
    


for line in sys.stdin:
    n, m = map(int, line.strip().split())
    print(dp(n, m))