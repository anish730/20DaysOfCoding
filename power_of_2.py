def power_of_2(n):
    return n > 0 and (n & (n - 1) == 0)

print(power_of_2(20))
print(power_of_2(32))
print(power_of_2(2640))
print(power_of_2(64))
print(power_of_2(123123))
print(power_of_2(128))
