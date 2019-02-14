import sys

for s in sys.stdin:
    num = s.split()
    name = num[0]
    if name == 'END':
        break
    mB = float(num[1])
    mV = float(num[2])
    delta = mB - mV

    if delta < -0.251:
        print('%s %.2lf O' % (name, delta))
    elif delta > -0.250 and delta < -0.001:
        print('%s %.2lf B' % (name, delta))
    elif delta > -0.001 and delta < 0.249:
        print('%s %.2lf A' % (name, delta))
    elif delta > 0.249 and delta < 0.499:
        print('%s %.2lf F' % (name, delta))
    elif delta > 0.499 and delta < 0.999:
        print('%s %.2lf G' % (name, delta))
    elif delta > 0.999 and delta < 1.499:
        print('%s %.2lf K' % (name, delta))
    elif delta > 1.499:
        print('%s %.2lf M' % (name, delta))
