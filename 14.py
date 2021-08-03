def collatz_length(n):
	length = 0
	while not n == 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n + 1
		length += 1
	return length

long_num = 1
long_chain = 0

for n in range(2, 1000000):
	if n % 5000 == 0:
		print(n)
	col_len = collatz_length(n)
	if col_len > long_chain:
		long_chain = col_len
		long_num = n

print(long_num)