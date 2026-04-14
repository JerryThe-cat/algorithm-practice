import sys
input = sys.stdin.readline
from array import array

def sort(nums, count):
    if len(nums) <= 1:
        return nums, count
    
    mid = len(nums) // 2
    left, count_l = sort(nums[:mid], 0)
    right, count_r = sort(nums[mid:], 0)

    return merge(left, right, count_l + count_r)

def merge(left, right, count):
    result = array('l')

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]);
            i += 1
        else:
            result.append(right[j]); 
            j += 1
            count += len(left) - i

            
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

for line in sys.stdin:
    n = int(line)
    nums = array('l', map(int, input().split()))
    result, count = sort(nums, 0)
    print(count)