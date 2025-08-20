def zero_sum_subarrays(arr):
    """
    Finds all subarrays with sum equal to zero without using extra space.
    
    Parameters:
    arr (list): List of integers
    
    Returns:
    list: List of tuples (start_index, end_index) of all zero-sum subarrays
    """
    n = len(arr)
    result = []

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum == 0:
                result.append((start, end))

    return result

arr1 = [1, 2, -3, 3, -1, 2]
print(zero_sum_subarrays(arr1)) 

arr2 = [4, -1, -3, 1, 2, -1]
print(zero_sum_subarrays(arr2))  

arr3 = [0, 0, 0]
print(zero_sum_subarrays(arr3))  
