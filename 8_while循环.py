##条件成立就一直做

answer = 56
guess = int(input("请猜测一个数字："))

while guess != answer:
    print("猜错")
    guess = int(input("请重新猜测一个数字："))

print("猜对了")