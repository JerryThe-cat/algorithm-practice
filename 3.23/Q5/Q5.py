def move(remain_plates, disk_id, counts, direction, path):
    #          ↑ 新增参数：当前最大盘子的编号
    start = direction[0]
    end = direction[1]
    mid = ({"A", "B", "C"} - {start} - {end}).pop()

    if remain_plates == 1:
        counts[0] += 1
        path.append((counts[0], disk_id, start, end))
        return

    move(remain_plates - 1, disk_id - 1, counts, [start, mid], path)
    move(1,                 disk_id,     counts, [start, end], path)
    move(remain_plates - 1, disk_id - 1, counts, [mid,   end], path)

N = int(input())
counts = [0]
path = []

move(N, N, counts, ["A", "C"], path)  # 初始时最大盘编号就是 N

print(counts[0])
for step, disk, src, dst in path:
    print(f"step {step}: {disk} From {src} To {dst}")
