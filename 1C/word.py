T = int(input())

from itertools import product

for case in range(T):
	
	N, L = [int(x) for x in input().split()]
	result = "-"
	words = []
	for i in range(N):
		words.append(input())
	letters = [set(x) for x in list(map(list, zip(*words)))]
	possible_words = [("").join(word) for word in list(product(*letters))]
	# products = list(product(*letters))
	# possible_words = [("").join(word) for word in products]

	for word in possible_words:
		if word not in words:
			result = word
			break
	
	print("Case #{}: {}".format(case + 1, result))
