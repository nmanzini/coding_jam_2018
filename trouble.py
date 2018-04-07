def TroubleSort(L,length):
	done = False
	while not done:
		done = True
		for n in range(length - 2):
			if L[n] > L[n+2]:
				done = False
				L[n], L[n+2] = L[n+2], L[n]
	return (L)

T = int(input())
for i in range(T):
	length = int(input())
	L = [int(n) for n in input().split(" ")]
	L_S = sorted(L)
	L_T = TroubleSort(L[:],length)
	result = "OK"
	for n in range(length):
		if L_S[n] != L_T[n]:
			result = n
			break
	print("Case #{}:".format(i + 1), result)
