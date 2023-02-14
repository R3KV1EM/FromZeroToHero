def highhest_even(*args):
	a = []
	for even_arg in args:
		if even_arg %2 == 0:
			a.append(even_arg)
	return max(a)

print(highhest_even(84,745,33,12,554,16,722))
#print(highhest_even(13, 2, 3, 10, 4, 8, 11))
