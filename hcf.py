def hcf(x, y):
    if x > y:
        smallest = y
    else:
        smallest = x

    for i in range(1, smallest+1):
        if ((x % i)== 0 and (y % i) == 0):
            hcf = i
    return hcf

print("The HCF is", hcf(64, 72))