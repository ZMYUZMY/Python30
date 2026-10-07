#元组用（）创建之后不能增加、删除、修改
points = (3, 4, 5)
print(points[1], points[-1])  # 输出: 4 5
#值一次赋给多个变量
x,y,z = points
print(x, y, z)  # 输出: 3 4 5


#集合用{}创建，集合中没有重复元素，自动去重，集合是无序的，不能用下标访问集合中的元素
nums = {1, 2, 2, 5, 5, 6}
print(nums)  # 输出: {1, 2, 5, 6}

#列表用set转为集合就能自动去重
liebiao = [1, 2, 2, 5, 5, 6]
print(set(liebiao))  # 输出: {1, 2, 5, 6}
print(list(set(liebiao)))  # 输出: [1, 2, 5, 6]