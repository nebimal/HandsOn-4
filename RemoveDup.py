def remove_duplicates(arr):
    if not arr: 
        return []
    result = [arr[0]]  
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]: 
            result.append(arr[i]) 
    return result

array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(remove_duplicates(array1))  
print(remove_duplicates(array2))  
