A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Matrix multiplication not possible. Columns of A must equal Rows of B.")
else:
    product_matrix = []
    for i in range(rows_A):
        row_result = [] 
        for j in range(cols_B):
            dot_product = 0 
           
            for k in range(cols_A):
                dot_product += A[i][k] * B[k][j]
                
            row_result.append(dot_product)
            
        product_matrix.append(row_result)

    print("Product Matrix:")
    for row in product_matrix:
        print(row)
