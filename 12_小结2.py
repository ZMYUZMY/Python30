pos = neg = zero = 0

for i in range(5):
    x = int(input("请输入一个整数："))
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1
print(f"正数{pos}, 负数: {neg}, 零: {zero}")