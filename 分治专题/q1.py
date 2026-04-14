import random
import sys
from array import array
input = sys.stdin.readline

def find_rank_k(nums, m):
    while True:
        random_num = random.choice(nums)
        
        bigger  = array('l')
        smaller = array('l')
        equal_c = 0
        
        for x in nums:
            if x > random_num:
                bigger.append(x)
            elif x == random_num:
                equal_c += 1
            else:
                smaller.append(x)

        if m <= len(bigger):
            nums = bigger
        elif m <= len(bigger) + equal_c:
            return random_num
        else:
            m -= len(bigger) + equal_c
            nums = smaller

n, m = map(int, input().split())
nums = array('l', (int(input()) for _ in range(n)))
print(find_rank_k(nums, m))