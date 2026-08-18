

rows = int(input("Enter no. of rows: "))
cols= int(input("Enter no. of cols : ") )

print("Enter elements of Matrix A:" )
A =[]
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[i][j]: ")))
    A.append(row)

print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"B[i][j]:  ") ))
    B.append(row) 


C= []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] - B[i][j])
    C.append(row)

print("\nMatrix Subtraction:")
for i in range(rows):
    for j in range(cols):
        print(C[i][j], end=" ")
    print()