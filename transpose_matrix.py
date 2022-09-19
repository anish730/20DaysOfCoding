X = [
    [1, 2],
    [3, 5],
    [2, 6]
]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0])) ]

for r in result:
    print(r)