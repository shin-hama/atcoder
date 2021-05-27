row, col = (int(c) for c in input().strip().split(" "))

matrix = [[int(i) for i in input().strip().split(" ")] for _ in range(row)]

row_sums = [0] * row
col_sums = [0] * col
for i in range(row):
    for j in range(col):
        row_sums[i] += matrix[i][j]
        col_sums[j] += matrix[i][j]

result = [
    [str(row_sums[i] + col_sums[j] - matrix[i][j]) for j in range(col)]
    for i in range(row)
]

print("\n".join([" ".join(line) for line in result]))
