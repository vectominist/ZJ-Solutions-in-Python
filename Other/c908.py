import sys
import math

EPS = 1e-9

def ABS(x):
	if x > 0:
		return x
	else:
		return -x

for s in sys.stdin:
	num = s.split()
	N = int(num[0])
	
	for i in range(N):
		s = sys.stdin.readline()
		num = s.split()
		x1 = float(num[0])
		y1 = float(num[1])
		R1 = float(num[2])
		x2 = float(num[3])
		y2 = float(num[4])
		R2 = float(num[5])
		d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
		if d - (R1 + R2) > EPS:
			print('No Intersect')
		elif (R1 > R2) and (R1 - R2 - d > EPS):
			print('No Intersect')
		elif (R2 > R1) and (R2 - R1 - d > EPS):
			print('No Intersect')
		elif ABS(d - (R1 + R2)) < EPS:
			x = (R1 * x2 + R2 * x1) / (R1 + R2)
			y = (R1 * y2 + R2 * y1) / (R1 + R2)
			print('%.3f %.3lf' % (x, y))
		elif (R1 > R2) and (ABS(R1 - R2 - d) < EPS):
			x = x1 + (x2 - x1) * R1 / d
			y = y1 + (y2 - y1) * R1 / d
			print('%.3f %.3lf' % (x, y))
		elif (R2 > R1) and (ABS(R2 - R1 - d) < EPS):
			x = x2 + (x1 - x2) * R2 / d
			y = y2 + (y1 - y2) * R2 / d
			print('%.3f %.3lf' % (x, y))
		else:
			if R1 < R2: # Make R1 > R2
				tmp = x1
				x1 = x2
				x2 = tmp
				tmp = y1
				y1 = y2
				y2 = tmp
				tmp = R1
				R1 = R2
				R2 = tmp
			
			cosa = (R1 ** 2 + d ** 2 - R2 ** 2) / (2 * R1 * d)
			#print(cosa)
			sina = math.sqrt(1 - cosa ** 2)
			
			Px = x1 + R1 * ( cosa * (x2 - x1) + sina * (y2 - y1)) / d
			Py = y1 + R1 * (-sina * (x2 - x1) + cosa * (y2 - y1)) / d

			Dx = x1 + R1 * ( cosa * (x2 - x1) - sina * (y2 - y1)) / d
			Dy = y1 + R1 * ( sina * (x2 - x1) + cosa * (y2 - y1)) / d

			if Px < Dx:
				print('%.3lf %.3lf %.3lf %.3lf' % (Px, Py, Dx, Dy))
			else:
				if ABS(Px - Dx) < EPS and (Py < Dy):
					print('%.3lf %.3lf %.3lf %.3lf' % (Px, Py, Dx, Dy))
				else:
					print('%.3lf %.3lf %.3lf %.3lf' % (Dx, Dy, Px, Py))
