class student:
    def __init__(self,name,age):        #属性挂在self上面
        self.name = name
        self.age = age          
    def x(self):                #方法第一个参数self
        print(f'我是{self.name},今年{self.age}岁')  
#两个对象
s1 = student('小明',20)
s2 = student('xioa',4)
s1.x()
s2.x()