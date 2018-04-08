import sys

T = int(input())
# print("T = ",T, file=sys.stderr)
for case in range(T):
	A = int(input())
	# print("A = ",A, file=sys.stderr)
	matrix = [[0 for i in range(1000)] for j in range(1000)]

	xi = 1
	yi = 1
	x = 1
	y = 1
	print (x + 1,y + 1)
	sys.stdout.flush()
	side_x = int(A / 3) + 1
	while xi != -1 and yi != -1:
		xi, yi = [int(x) - 1 for x in input().split(" ")]
		if xi < 0 or yi < 0:
			# print("break",xi,yi, file=sys.stderr)
			break
		matrix[xi][yi] = 1
		# print("received Position ",xi,yi, file=sys.stderr)
		skip = sum(matrix[x-1][:3])

		if skip == 3 and x < side_x - 1:
			x += 1
			print (x + 1,y + 1)
			sys.stdout.flush()
		else:
			print (x + 1,y + 1)
			sys.stdout.flush()
# 	print("Out of WHILE ",xi,yi, file=sys.stderr)
# print("Out of TOTAL ",xi,yi, file=sys.stderr)