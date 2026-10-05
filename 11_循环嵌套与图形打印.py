#外层循环管第几行，内层循环管每一行的列数
for i in range(2):
    for j in range(3):
        print('*' ,end=' ')
    print()  ##换行


n = int(input("请输入一个整数："))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        print('*',end=' ')
    print()  ##换行