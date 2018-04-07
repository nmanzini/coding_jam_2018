T = int(input())

def return_damages(P):
	damages = 1
	total_damages = 0
	for n,a in enumerate(P):
		if a == "C":
			damages *= 2
		elif a == "S":
			total_damages += damages
	return total_damages, damages

def return_combination_n(P):
	switches_list = []
	for n,a in enumerate(P):
		if a == "C":
			switches = sum([1 for n,l in enumerate(P[n:]) if l =="S"])
			switches_list.append(switches)
	return (sum(switches_list))

def solver(P, D):
	P = list(P)
	combination_n = return_combination_n(P)

	total_damages, damages = return_damages(P)

	if (D - total_damages >= 0):
		return 0
	else:
		if combination_n == 0:
			return "IMPOSSIBLE"
		else:
			for c in range(combination_n):
				for n,a in enumerate(P[:-1]):
					if P[n] == "C" and P[n +1] == "S":
						P[n] = "S"
						P[n +1] = "C"
						break
				total_damages, damages = return_damages(P)

				if total_damages <= D:
					return (c + 1)
			return "IMPOSSIBLE"


for i in range(T):
	D, P = input().split(" ")
	D = int(D)
	print("Case #{}:".format(i + 1), solver(P, D))