from sympy import isprime

sum = []
n, m = map(int, input().split())
nums = list(map(int, input().split()))[:n]

def select(m, nums, add, sum):
    if m == 0:
        sum.append(add)
        return
    
    for i in range(len(nums)):
        select(m - 1, nums[i + 1:], add + nums[i], sum)

    return

select(m, nums, 0, sum)

p = 0
for i in range(len(sum)):
    if isprime(sum[i]):
        p += 1

print(p)