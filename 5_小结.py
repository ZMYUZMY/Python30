name =input("商品名：")
price = float(input("商品价格："))
num = int(input("购买数量："))

total = price * num
print(f"商品名：{name}，商品价格：{price}，购买数量：{num}，总价：{total}")