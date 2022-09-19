# 2x3 matrix
X = [
    [12,7,3],
    [4 ,5,6],
    ]
# 3x2 matrix
Y = [
    [5,8],
    [6,7],
    [4,5]
    ]
# result is 2x2
result = [
    [0,0],
    [0,0]
    ]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)