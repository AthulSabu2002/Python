def max_subarray_sum(arr):
    # Initialize variables
    max_current = arr[0]
    max_global = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update max_current to either the current element or the sum of current and previous subarray
        max_current = max(arr[i], max_current + arr[i])
        
        # Update max_global if the current subarray sum is greater than the global maximum
        if max_current > max_global:
            max_global = max_current

    return max_global

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print(f"The maximum subarray sum is: {result}")
