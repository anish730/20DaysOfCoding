def quad_eq(a,b,c):
    eq1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
    eq2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
    print("the solutions are {0} and {1} ".format(eq1, eq2))

quad_eq(1,5,6)

