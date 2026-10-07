#固定模板 with open('文件名', 'w', encoding='utf-8') as f:
#    f.write('内容')    'w'写入 'a'追加 'r'读取 encoding='utf-8'指定编码格式.
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('This is a test file.\n')
#读内容
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

#按行读取
with open('test.txt', 'r', encoding='utf-8') as f:
    for i,line in enumerate(f,1):
        print(f"{i}: {line.strip()}")  # strip()去掉换行符
