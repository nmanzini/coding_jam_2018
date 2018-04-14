T = int(input())

for case in range(T):
	R, B, C = [int(n) for n in input().split(" ")]
	cashiers = []
	for asd in range(C):
		M,S,P = [int(n) for n in input().split(" ")]
		casher = {}
		casher["M"] = M
		casher["S"] = S
		casher["P"] = P
		cashiers.append(casher)
	for c in cashiers:
		result = []
		for b in range(1, c["M"] + 1):
			result.append(c["S"] * b + c["P"])
		c["R"] = result
		print(result)
	cashiers_used = []
	# for b in B:
	# 	fastests = [c["R"][0] for x in cashiers]
	# 	cashier = fastests.index(min(fastests))
	# 	cashiers_used.append(cashier)
	# 	cashiers[cashier].pop(0)
	B_left = B
	times = []
	while B_left > 0 and R > 0:
		ratio_times = []
		items_list = []

		for cashier in cashiers:
			items = len(cashier["R"])
			if items  <=  B_left:
				items_list.append(items)
				last_time = cashier["R"][-1]
				ratio_times.append(last_time / items)
			else:
				items = B_left
				items_list.append(items)
				last_time = cashier["R"][items - 1]
				ratio_times.append(last_time / B_left)
		ratio = min(ratio_times)
		cashier_i = ratio_times.index(ratio)
		items = items_list[cashier_i]
		
		if items < B_left:
			time = cashiers[cashier_i]["R"][-1]
		else:
			time = cashiers[cashier_i]["R"][B_left - 1]
		B_left -= items
		times.append(time)
		del cashiers[cashier_i]
		R -= 1
		print("items",items,"i", cashier_i, "B_left",B_left)
	print("times",times)
	print("Case #{}: {}".format(case + 1, max(times)))


		

	






