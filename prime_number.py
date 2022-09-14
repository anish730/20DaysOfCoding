def prime_number(n):
    if n > 1:
        for num in range(2, n):
            if n % num == 0 :
                return "Not Prime"
            else:
                return "Prime"

print(prime_number(10))
print(prime_number(100))
print(prime_number(23))
print(prime_number(53))
print(prime_number(77))