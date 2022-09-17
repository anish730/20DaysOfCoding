num = int(input("Enter a number: "))

sum=0
power = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**power
    temp = temp // 10

if num == sum:
    print("The number is armstrong")
else:
    print("The number is not armstrong")