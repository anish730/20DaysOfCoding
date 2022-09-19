X = [
    [1, 2, 3],
    [3, 5, 8],
    [4, 7, 9]
]

Y = [
    [6, 8, 3],
    [3, 6, 2],
    [0, 5, 8]
]

result = [ [ X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)
