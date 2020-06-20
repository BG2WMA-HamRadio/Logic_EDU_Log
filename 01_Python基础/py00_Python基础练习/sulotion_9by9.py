# 使用while循环的方法：
# 初始化被乘数
i = 0

#建立循环
while i < 9:
    i += 1
    # 初始化乘数
    j = 1
    # 建立内部循环：
    while j <= i:
        # 格式化字符并打印结果，当j > i时退出循环
        # 循环内部不换行
        print(f'{j} * {i} = {j*i} ', end='')
        # 更新变量
        j += 1
    # 当前内部循环结束后，换行
    print()


# 使用for循环的方法：
# 遍历1~9，range函数不包含结束。
for i in range(1, 10):
    # 遍历 1~i，并打印结果
    for j in range(1, i+1):
        print(f'{j} * {i} = {j*i} ', end='')
    # 内部循环结束后，换行
    print()
