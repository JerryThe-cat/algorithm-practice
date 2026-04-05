N = int(input())

result = []

remain = list(range(1, N + 1))

def rank_all(remain,path):
    # 终止条件：remain_num为空
    if not remain:
        result.append(path)
        return result

    # 递归调用：
    for i in range(len(remain)):
        rank_all(remain[:i] + remain[i+1:],path *10 + remain[i])
    
    return

rank_all(remain, 0)

for p in result:
    print(p)