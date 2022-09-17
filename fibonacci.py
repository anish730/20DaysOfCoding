nth = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nth <=0:
    print("Enter positive number")
elif nth == 1:
    print(n1)
else:
    print("Fibonacci sequence :")
    while count < nth:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n 
        count+=1