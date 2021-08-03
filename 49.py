def is_prime(n):
	for i in range(3, int(n**(0.5))+1, 2):
		if n % i == 0:
			return False
	return True

def bin_search(l, r, target, arr):
	if r < l:
		return -1
	mid = int((l + r) / 2)
	if arr[mid] == target:
		return mid
	elif arr[mid] < target:
		return bin_search(mid + 1, r, target, arr)
	else:
		return bin_search(l, mid - 1, target, arr)

def are_numbers_permutations(a, b, c):
	a_str = str(a)
	b_str = str(b)
	c_str = str(c)
	for i in range(len(a_str)):
		if not (
				a_str[i] in b_str and a_str[i] in c_str
				and b_str[i] in a_str and b_str[i] in c_str
				and c_str[i] in b_str and c_str[i] in a_str):
			return False
	return True

primes = []
for i in range(1001, 10000, 2):
	if is_prime(i):
		primes.append(i)

start_index = 0
indices = []
found = False
while start_index < len(primes):
	for i in range(start_index + 1, len(primes) - 1):
		first_dist = primes[i] - primes[start_index]
		first_is_prime = not bin_search(i, len(primes) - 1, primes[i], primes) == -1
		second_is_prime = not bin_search(i, len(primes) - 1, primes[i] + first_dist, primes) == -1
		if first_is_prime and second_is_prime:
			if are_numbers_permutations(
					primes[start_index],
					primes[start_index] + first_dist,
					primes[start_index] + (2 * first_dist)):
				print(
						primes[start_index],
						primes[start_index] + first_dist,
						primes[start_index] + (2*first_dist))
				indices.append(start_index)
	start_index += 1

