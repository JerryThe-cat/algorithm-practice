n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

found = False
for mask in range(1 << n):  # 枚举所有子集
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += nums[i]
    if total == k:
        found = True
        break

print("YE5" if found else "N0")
