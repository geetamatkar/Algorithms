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

'''
Time Comlpexity :
    The time complexity of selection sort is O(n^2), where n is the number of elements in the array.
    In the worst-case scenario, selection sort requires two nested loops. O(n^2)
    The best-case time complexity of selection sort is also O(n^2). Even if the input array is already sorted, the algorithm will still 
    perform the same number of iterations as in the worst case because it needs to check all elements to confirm their relative order.


Space Complexity : 
    The space complexity of selection sort is O(1), which means it uses a constant amount of additional space regardless of the input size.
'''