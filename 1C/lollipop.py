import sys

T = int(input())

for case in range(T):
	n = int(input())
	lollipops = [i for i in range(n)]
	asked = [[i,0] for i in range(n)]
	for c in range(n):
		prefs = [int(i) for i in input().split()]
		if prefs[0] == 0:
			print("-1")
			sys.stdout.flush()
		else:
			submitted = False
			for i in prefs[1:]:
				for l in asked:
					if l[0] == i:
						l[1] += 1
			asked.sort(key=lambda x: x[1])
			# if c == 0:
			# 	print(prefs[1])
			# 	lollipops.remove(prefs[1])
			# 	sys.stdout.flush()
			# 	submitted = True
			# else:
			if case == 4:
				print(asked, file=sys.stderr)
			for l in asked:
				if l[0] in lollipops and l[0] in prefs[1:]:
					lollipops.remove(l[0])
					print(l[0])
					sys.stdout.flush()
					submitted = True
					break
			if not submitted:
				print("-1")
				sys.stdout.flush()
	# print(asked, file=sys.stderr)
exit()


