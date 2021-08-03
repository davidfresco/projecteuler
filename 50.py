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

primes = []
for i in range(1, 1000000, 2):
	if is_prime(i):
		primes.append(i)

longest_sum_prime = 0
sum_length = 0
long_sum_start = 0
for start_index in range(0, len(primes)):
	sum = 0
	length = 0
	while sum < 1000000 and len(primes) > start_index + length:
		sum += primes[start_index + length]
		length += 1
		if bin_search(start_index, len(primes)-1, sum, primes) > -1:
			if length >= sum_length:
				sum_length = length
				longest_sum_prime = sum
				long_sum_start = start_index

print(longest_sum_prime, sum_length, long_sum_start)
sum = 0
for i in range(sum_length):
	sum += primes[i + long_sum_start]
print(sum)