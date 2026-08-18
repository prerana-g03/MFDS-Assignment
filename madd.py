rows = int(input("enter rows: "))
cols = int(input ("enter cols: "))
print(" enter elements of matrix A:")
A= []
for i in range(rows):
    row= []
    for j in range(cols):
        row.append(int(input(f"A[i][j]: ")))
    A.append(row)
print("Enter elements of matrix B:" )
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"B[i][j]: ")))
    B.append(row)
C= []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("\n matrix addition:")
for i in range(rows):
    for j in range(cols):
        print(C[i][j], end=" ")
    print()