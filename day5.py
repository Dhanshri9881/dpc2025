def leaders(arr):
    n = len(arr)
    res = []
    max_right = arr[-1]
    res.append(max_right)

    for i in range(n-2, -1, -1):
        if arr[i] >= max_right:
            res.append(arr[i])
            max_right = arr[i]
    return res[::-1]   

print(leaders([16, 17, 4, 3, 5, 2]))      
print(leaders([1, 2, 3, 4, 0]))          
print(leaders([7, 10, 4, 10, 6, 5, 2]))   
print(leaders([5]))                       
print(leaders([100, 50, 20, 10]))         
