import sys

ans = ['豬', '鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗']

for s in sys.stdin:
    num = s.split()
    n = int(num[0])
    if n < 0:
        n += 1
    print(ans[(n + 120) % 12])
