import math
import itertools
def primes():
	i = 2
	while True:
		if (math.factorial(i - 1) + 1) % i != 0:
			i += 1
		else:
			yield i
			i += 1
print(list(itertools.takewhile(lambda x : x <= 95, primes())))

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]