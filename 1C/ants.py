T = int(input())

def weight_test_nicola(sub_ants):
	for n,weight in enumerate(sub_ants[:-1]):
		# print(weight*6 ,">=", sum(ants[n+1:]))
		if (weight * 6) < sum(sub_ants[n+1:]):
			return(False)
	return (True)

for case in range(T):
	N = int(input())
	ants = [int(i) for i in input().split(" ")][::-1]
	result = 1
	for i in range(1,N + 1):
		if weight_test_nicola(ants[:i]):
			result = i
		else:
			break
	print("Case #{}: {}".format(case + 1, result))

