
def prime(x):
	if x<2:
		return 0
	else:
		for y in range(2, int(x**0.5)+1):
			if not x%y:
				return 0
		return 1

def primefactors(n):
	while n>1:
		for x in range(2, int(n)+1):
			if not n%x and prime(x):
				yield x
				n /= x
				break
			else:
				pass

print(list(primefactors(int(input(">>")))))

