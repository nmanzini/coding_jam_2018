import math

# SORRY EVERYONE
# this code is incredibly messy and the solution is quite rough
# not my best opus

T = int(input())

for case in range(T):
	A = float(input())

	a = [0.5, 0.0, 0.0]
	b = [0.0, 0.5, 0.0]
	c = [0.0, 0.0, 0.5]



	angle1_min = 0
	angle1_max = math.pi/4
	angle1 = angle1_min + (angle1_max - angle1_min)/2

	if A <= 1.414213:

		area = math.cos(angle1) + math.sin(angle1)
		while abs(A - area) > 0.00000001:
			if A > area:
				angle1_min = angle1
			else:
				angle1_max = angle1
			angle1 = angle1_min + (angle1_max - angle1_min)/2
			area = math.cos(angle1) + math.sin(angle1)

		a[0] = math.cos(angle1) * 0.5
		a[1] = math.sin(angle1) * 0.5
		b[0] = -math.sin(angle1) * 0.5
		b[1] = math.cos(angle1) * 0.5
	else:

		angle1_max = math.pi/36 * 7.1 
		angle1 = angle1_min + (angle1_max - angle1_min)/2

		frtyfive = math.pi/4
		area1 = math.cos(frtyfive) + math.sin(frtyfive)
		area = math.cos(angle1) * area1 + math.sin(angle1)

		i = 0

		while abs(A - area) > 0.00000001 and i != 30:
			i += 1
			if A >= area:
				angle1_min = angle1
			else:
				angle1_max = angle1
			angle1 = angle1_min + (angle1_max - angle1_min)/2
			area = math.cos(angle1) * area1 + math.sin(angle1)

		a[0] = math.cos(frtyfive) * 0.5
		a[1] = math.sin(frtyfive) * 0.5 * math.cos(angle1)
		a[2] = -math.sin(angle1) * 0.5 * math.cos(frtyfive)

		b[0] = -math.sin(frtyfive) * 0.5
		b[1] = math.cos(frtyfive) * 0.5 * math.cos(angle1)
		b[2] = -math.sin(angle1) * 0.5 * math.cos(frtyfive)

		c[0] = 0.0 
		c[1] = math.sin(angle1) * 0.5
		c[2] = math.cos(angle1) * 0.5


	print("Case #{}:".format(case + 1))
	print(a[0], a[1], a[2])
	print(b[0], b[1], b[2])
	print(c[0], c[1], c[2])