n = int(input())
nums = list(map(int, input().split()))

def MSS(nums):
    if len(nums) == 1:
        return nums[0]
    
    mid = len(nums) // 2
    LMS = MSS(nums[:mid])# 左边最大子段和
    RMS = MSS(nums[mid:])# 右边最大子段和
    
    LCP, RCP = [], []
    sum_L = sum_R = 0
    # 比较左边
    for i in range(mid - 1, -1, -1):
        sum_L += nums[i]
        LCP.append(sum_L)
    # 比较右边 
    for i in range(mid, len(nums)):
        sum_R += nums[i]
        RCP.append(sum_R) 
    MMS = max(LCP) + max(RCP)

    return max(LMS, RMS, MMS)

print(MSS(nums))