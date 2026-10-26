N = int(input("Enter the integer value of N: "))

is_n_prime = True
if N < 2:
    is_n_prime = False
else:
    i = 2
    while i * i <= N:
        if N % i == 0:
            is_n_prime = False
            break
        i += 1
if is_n_prime:
    print(f"{N} is prime.")
else:
    print(f"{N} is not prime.")

primes_list = []
total_sum = 0
num = 2
while num <= N:
    current_is_n_prime = True
    j = 2
    while j * j <= num:
        if num % j == 0:
            current_is_n_prime = False
            break
        j += 1

    if current_is_n_prime:
        primes_list.append(num)
        total_sum += num
    num += 1

print(f"Primes up to {N}: {primes_list}")
print(f"Sum of primes: {total_sum}")