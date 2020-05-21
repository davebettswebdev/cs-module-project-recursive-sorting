# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # Your code here
    i = 0
    j = 0
    while len(merged_arr) < elements:
        if i >= len(arrA):
            merged_arr.append(arrB[j])
            j+=1
        elif j >= len(arrB):
            merged_arr.append(arrA[i])
            i+=1
        elif arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    return merged_arr


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # two iterators for traversing the two halves
        i = 0
        j = 0

        # iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                # the value from the left half has been used 
                arr[k] = left[i]
                # move the iterator forward 
                i +=1
            else:
                arr[k] = right[j]
                j += 1
            # move to next slot
            k += 1
        # for all the ramaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
    # if the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return
    # two pointers to maintain start of both arrays to merge 
    while (start <= mid and start2 <= end):
        # if element 1 is in the right place
        if (arr[start] <= arr[start2]):
            start += 1
        else: 
            value = arr[start2]
            index = start2
            # shift all the elements between element 1 and element 2, right by 1 
            while (index != start):
                arr[index] = arr[index - 1] 
                index -= 1
            arr[start] = value
            # update all the pointers
            start += 1 
            mid += 1
            start2 += 1


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 
        m = l + (r - l) // 2 # splits array into 2 
        merge_sort_in_place(arr, l, m) # sorts first and second halves 
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
