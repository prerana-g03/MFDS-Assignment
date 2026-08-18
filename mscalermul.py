r=int(input("  enter rows: "))
c= int(input("enter cols: "))
matrix = []
print("enter matrix elements:")
for i in range(r):
    row = []
    for j in range(c):
        value = int(input())
        row.append(value)
    matrix.append(row)
scalar = int(input(" enter value: "))
for i in range(r):
    for j in range(c):
        matrix[i][j] = matrix[i][j] * scalar
print(" result:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()