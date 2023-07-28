def insertion_sort(arr):
    for i in range (1,len(arr)):
        key=arr[i]

        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    return arr

arr=[4,2,15,54,23,11]
print("Sorted array: ", insertion_sort(arr))


"""
Time complexity:
Worst case, Average case : O(n^2)
Best case : O(n) Input already sorted

Space complexity:
The space complexity of insertion sort is O(1) because the algorithm only requires a constant amount of additional memory space to 
perform the sorting.
"""