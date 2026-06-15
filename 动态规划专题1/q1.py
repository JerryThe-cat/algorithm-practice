n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

def max_subarray(nums):
    cur = ans = nums[0]
    for i in nums[1:]:
        cur = max(cur + i, i)
        ans = max(ans, cur)
    return ans

print(max_subarray(nums))