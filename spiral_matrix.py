def print_spiral_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            # Traverse left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            # Traverse up
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    # Print the matrix
    for row in matrix:
        print(" ".join(f"{x:2d}" for x in row))

# Test the function
print_spiral_matrix(4)
print("\n")
print_spiral_matrix(5)