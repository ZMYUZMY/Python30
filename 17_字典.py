#列表靠位置，字典靠键找
student = {"name": "小明", "age": 20, "grade": 85}
print(student["name"])  # 输出: 小明    
print(student["age"])   # 输出: 20
print(student["grade"]) # 输出: 85

#用[]访问字典中不存在的键会报错
#用get()访问字典中不存在的键，会返回None，也可以自己设置默认值。
print(student.get("name"))  # 输出: 小明
print(student.get("zzz",0))  # 没有这个键，返回默认值0
print(len(student))

#增删改查

d = {"name": "小明", "age": 20, "grade": 85}
d["gender"] = "男"  # 增加键值对
d["age"] = 21      # 修改键值对
d.pop("grade")     # 删除键值对
del d["age"]      # 删除键值对
print(d)  # 输出: {'name': '小明', 'gender': '男'}
print("name" in d)  # 输出: True

xinxi = {'小明':'1870000000','小红':'1870000001','小刚':'1870000002'}

for name in xinxi:
    print(f"{name}: {xinxi[name]}")  # 输出: 小明: 1870000000 小红: 1870000001 小刚: 1870000002

key = input("请输入要查询的姓名：")
if key in xinxi:
    print(xinxi[key])
else:
    print("未找到该姓名。")