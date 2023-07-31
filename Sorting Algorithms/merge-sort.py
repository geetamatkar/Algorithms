def merge_sort(arr):
    if len(arr)>1:
        mid= len(arr)//2
    
        L= arr[ :mid]
        R= arr[mid: ]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

        return arr


arr=[52,2,76,15,35,12,3]
print("Sorted array: ", merge_sort(arr))


'''
Time complexity:
Merge Sort has a time complexity of O(n log n), where 'n' is the number of elements in the input array. 
This complexity arises from the fact that the array is recursively divided into halves until the base case is reached

Space complexity:
Merge Sort has a space complexity of O(n) due to the need for additional space to hold the temporary arrays during the merging process. 
'''

