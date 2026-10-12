matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [10, 20, 30]
]

for row in range(len(matrix)):
    row_sum = 0
    
    for col in range(len(matrix[row])):
       row_sum += matrix[row][col]

    print(f"Row {row + 1} sum: {row_sum}")