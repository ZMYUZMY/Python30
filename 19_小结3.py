def analyze(scores):
    return {
        '最高': max(scores),
        '最低': min(scores),
        '平均': sum(scores) / len(scores)
    }
results = analyze([88, 92, 79, 95, 85])
for k in results:
    print(f"{k}: {results[k]}")