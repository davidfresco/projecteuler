
def num_factors(n):
    factors = 0
    for i in range(1, int(n**(0.5)) + 1):
        if not n % i:
            factors += 2
    return factors

i = 1
pyramid_num = 1
while num_factors(pyramid_num) < 500:
    i += 1
    pyramid_num += i

print(pyramid_num)