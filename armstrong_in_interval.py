f = int(input("From: "))
to = int(input("To: "))


for num in range(f, to+1):
    sum = 0
    power = len(str(num))
    temp = num 
    while temp > 0:
        digit = temp % 10
        sum += digit**power 
        temp = temp // 10

    if num == sum:
        print(num)