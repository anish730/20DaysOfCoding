def area(a, b,c):
    s = (a+b+c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

print(area(5,4,3))