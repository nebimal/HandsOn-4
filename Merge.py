def MergeSort(arrays):
    k = len(arrays) 
    n = len(arrays[0]) if k > 0 else 0  
    index = [0] * k 
    result = []
    while len(result) < n * k:
        min_val = float('inf')
        min_index = -1 
        for i in range(k):
            if index[i] < n and arrays[i][index[i]] < min_val:
                min_val = arrays[i][index[i]]
                min_index = i
        result.append(min_val)
        index[min_index] += 1

    return result

array1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
array2 = [[1, 3, 7], [2, 4, 8], [9, 10, 11]]

print(MergeSort(array1))  
print(MergeSort(array2))
