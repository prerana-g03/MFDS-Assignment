n = int(input(" enter size of matrix: "))
matrix = []
print(" enter matrix elements:")
for i in range(n):
    row = []
    for j in range( n):
        value = int( input())
        row.append(value )
    matrix.append( row)
trace = 0
for i in range(n):
    trace = trace + matrix[i][i]
print("Trace =", trace)