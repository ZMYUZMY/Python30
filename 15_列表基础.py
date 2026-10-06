fruits = ['苹果', '香蕉', '橘子', '葡萄', '西瓜']


fruits[0] = '草莓'
fruits.append('菠萝')
fruits.remove('香蕉')

fruits.pop()  # 删除最后一个元素
print(len(fruits))
print(fruits[0])
print(fruits[3])

for s in fruits:
    print(s,end=' ')
print()

for i in range(len(fruits)):
    print(f'第{i+1}个水果是：{fruits[i]}',end=' ')