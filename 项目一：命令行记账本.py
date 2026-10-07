import json

FILE = 'account.json'

def load_records():
    try:
        with open(FILE,'r',encoding='utf-8') as f:
            return json.load(f)

    except:
        return[]
def save_records(records):
    with open(FILE,'w',encoding='utf-8') as f:
        json.dump(records,f,ensure_ascii=False)

records = load_records()
for money, note in [(12.5,'午饭'),(11,'奶茶'),(56,'聚餐')]:
    records.append({'金额':money,'备注':note})
save_records(records)

for i,r in enumerate(records,1):
    print(f'{i},{r['备注']}:{r['金额']}元')

total = sum(r['金额'] for r in records)
print(f'共{len(records)}笔，合计{total}元')

biggest = max(records,key=lambda r:r['金额'])
print(f'最贵的一笔:{biggest['备注']}{biggest['金额']}')