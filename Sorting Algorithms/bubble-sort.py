def bubble_sort(arr):
    n= len(arr)

    for i in range(n):
        for j in range (n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



arr=[54,76,12,43,8,33]
print("Sorted arraay: ", bubble_sort(arr))

   

'''
Time complexity:
The time complexity of the bubble sort algorithm is O(n^2)
The best-case time complexity of bubble sort is O(n). This occurs when the array is already sorted, and no swaps are needed in any pass.
However, bubble sort still requires scanning the entire array in each pass to determine if any swaps are necessary

Space complexity:
The space complexity of bubble sort is O(1) because it operates directly on the input array without requiring additional space that grows 
with the input size. 

'''