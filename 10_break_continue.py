##break跳出整个循环
##continue只结束本轮,然后回到条件判断继续判断条件
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i,end=' ')

n = int(input("请输入一个整数："))
is_prime = True

for i in range(2,int(n ** 0.5)+1):
    if n % i == 0:
        is_prime = False
        break
print(f'{n}'+('是素数'if is_prime else '不是素数'))

