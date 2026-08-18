

rows = int(input("enter rows: "))
cols = int(input(" enter  cols : "))

A= []

print(" enter elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[i][j]: ")) )
    A.append(row)

T= []

for j in range(cols):
    row =[]
    for i in range(rows):
        row.append(A[i][j])
    T.append(row)

print("\n matrix:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j], end=" ")
    print()


print("\n transpose matrix:")
for i in range(cols):
    for j in range(rows):
        print(T[i][j], end=" ")
    print()