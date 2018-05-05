T = int(input())

for case in range(T):
	N = int(input())
	ants = [int(i) for i in input().split()]
	ants = ants[::-1]
	result = 0
	failed = False
	for sub_ants in [ants[0:i + 1] for i in range (N)]:
		for n,ant in enumerate(sub_ants[:-1]):
			if ant * 6 < sum(sub_ants[n + 1:]):
				failed = True
				result = len(sub_ants)
				break
		if failed:
			break

	print("Case #{}: {}".format(case + 1, result))
