s, k = input().split()
k = int(k)

def search_code(s, k):
    l = len(s)
    while l < k:
        l *= 2
    
    while l >= k:
        if l == len(s):
            return s[k - 1]

        elif k <= (l // 2):
            l //= 2

        else:
            k -= l // 2
            k = (k - 2) % (l // 2) + 1
            l //= 2

print(search_code(s, k))


#先把长度翻倍到能覆盖k
#然后不断折半，把 k 映射回原串
# if:落在前半，什么都不用做，继续缩
# else:落在后半（旋转串），换算下标