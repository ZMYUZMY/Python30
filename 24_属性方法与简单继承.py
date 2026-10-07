#继承：站在父类肩膀上，自动拥有父类的属性和方法
class a:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name}在吃东西')

class b(a):
    def bark(self):
        print(f'{self.name}wan')

d = b('1')
d.eat()     #父类继承
d.bark()    #自己新增方法

#重写
class c(b):
    def bark(self):
        print(f'{self.name}lili')

        
#super().方法()调用父类的方法
class c(b):
    def bark(self):
        super().bark()
        print(f'{self.name}56')
d1 = c('yu')
d2 = c('yi')
d1.bark()
d2.bark()