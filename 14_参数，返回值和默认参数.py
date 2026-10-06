def greet(name):
    print(f"Hello, {name}!")
greet("小明")
greet("小红")

def add(a, b):
    print(a + b)

add(3, 5)
add(100, 200)


#默认参数必须放最后
def power(x,n=2):
    return x ** n
print(power(3))
print(power(2, 4))


def intro(name, age=18):
    print(f"大家好，我叫{name}，今年{age}岁。")

intro("小明")
intro("小红", 20)