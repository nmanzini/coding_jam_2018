T = int(input())

for case in range(T):
	R, C, H, V = [int(n) for n in input().split(" ")]
	matrix = []
	total = 0
	result = "POSSIBLE"
	for i in range(R):
		matrix.append(input())
		total += matrix[i].count('@')
	each_choco = total /( H + 1) / (V + 1)
	if each_choco % 1 != 0:
		result = "IMPOSSIBLE"
	somma = 0
	per_row = total / (H + 1)
	per_col = total / (V + 1)
	row_index = [0]
	col_index = [0]
	# print("per_row",per_row)
	# print("per_col",per_col)
	for i in range(R):
		somma +=  matrix[i].count('@')
		# print("row", i, somma)
		if somma == per_row:
			somma = 0
			row_index.append(i+1)
		elif somma < per_row:
			continue
		elif somma > per_row:
			result = "IMPOSSIBLE"
	# if somma != per_row:
	# 	result = "IMPOSSIBLE"
	somma = 0
	
	for j in range(C):
		for i in range(R):
			somma +=  matrix[i][j].count('@')
		if somma == per_col:
			somma = 0
			col_index.append(j+1)
		elif somma < per_col:
			continue
		elif somma > per_col:
			result = "IMPOSSIBLE"
	if result == "POSSIBLE":
		for i in range( H + 1 ):
			for j in range( V + 1):
				somma = 0
				for r in range(row_index[i],row_index[i+1]):
					for c in range(col_index[j],col_index[j+1]):
						somma +=  matrix[r][c].count('@')
				if somma != each_choco:
					result = "IMPOSSIBLE"
	print("Case #{}: {}".format(case + 1, result))
