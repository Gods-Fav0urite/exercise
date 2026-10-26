matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [10, 20, 30]
]

num_rows = len(matrix)
num_cols = len(matrix[0]) if num_rows > 0 else 0

for row in range(len(matrix)):
    row_total = 0
    
    for col in range(len(matrix[row])):
       row_total += matrix[row][col]

    print(f"Row {row + 1} total: {row_total}")