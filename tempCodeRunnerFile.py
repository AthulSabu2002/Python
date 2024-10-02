        for j in range(len(triangle[i])):  # Iterate over all elements in the current row
                print(min(triangle[i+1][j], triangle[i+1][j+1]))