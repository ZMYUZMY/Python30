year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")