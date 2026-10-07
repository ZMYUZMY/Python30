try:
    x = int('abc')  # 这里会引发 ValueError 异常
    print('zhixing')
except :
    print("输入的不是一个有效的整数。")

print("程序继续运行...")

try:
    a = float(input('被除数：'))
    b = float(input('除数：'))
    print(f"{a} / {b} = {a / b}")
except ValueError:
    print("输入的不是一个有效的数字。")
except ZeroDivisionError:
    print("除数不能为零。")