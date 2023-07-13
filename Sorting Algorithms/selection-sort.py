def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = [5,8,2,45,21,4]
print("Sorted array: ", selection_sort(arr))