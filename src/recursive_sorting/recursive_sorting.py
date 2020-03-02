# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):  # this part takes two lists/arrays and merges them and returns the new array. this is the helper for the function below
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # declare the starting indicies for below so that it will move along the index in each array/list at the same time the main loop proceeds
    a = 0
    b = 0
    for i in range(elements):  # so far its only adding on thing to the merged array... which means it's adding only in the one item at the arr index of 0 then
        #this checks to see if one left or right is empty and then uses the other array to add to merged_arr
        # if a >= len(arrA):#if the initial value "0" is greater or equal to the length of arrA the use arrB and increment b to input from the next indicie from arrB
        #     merged_arr[i] = arrB[b]
        #     b += 1 # this allows for movement through the right side split arr and moves to next index so that it doesn't continue adding the smallest number instead
        # elif b >= len(arrB):#if the initial value "0" is greater or equal to the lenth of arrB then use arrA and increment a to input from the next indicie from arrA
        #     merged_arr[i]=arrA[a]
        #     a +=1 #this allows for movement through the left side split arr and moves to next index so that it doesn't continue adding the same smallest number
        # #now that we have checked for one being empty we need to then append the smallest whether it's from arrA or arrB
        # elif arrA[a] < arrB[b]:
        #     merged_arr[i]= arrA[a]
        #     a+=1 #this allows for movement through the left side split arr and moves to next index so that it doesn't continue adding the same smallest number
        # else:
        #     merged_arr[i] = arrB[b]
        #     b+=1 # this allows for movement through the right side split arr and moves to next index so that it doesn't continue adding the smallest number instead


        ### 
        # BELOW IS MY VERSION: I was getting the length and matching with a/b count but wasn't using it properly... 
        # had it looking for a 0 length instead of using the count to verify that it wouldn't try to continue past the length of arrA/arrB
        #----- the use of that count was what i was missing. 
        ###
        #the first two should basically check for empty list/array and then use the other
        if len(arrA) <= a:
            merged_arr[i] = arrB[b]
            b +=1
        elif len(arrB) <=b:
            merged_arr[i] = arrA[a]
            a +=1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a+=1
        elif arrB[b] < arrA[a]:
            merged_arr[i] = arrB[b]
            b+=1
    print('merged_arr in merge function: ', merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print('arr:', arr)
    # TO-DO
    if len(arr) <= 1: #returns here is the list is already a length of 1 or less.. there is no need at that point to split
        return arr
    # split in half until it is down to left versus right with only one item in each to compare
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    print('left:', left, 'right:', right)
    # as it does this recursively it should look at both sides and continue comparing

    return merge(left, right)


list = [3, 1, 5, 9, 7, 6, 4, 2, 8]
print(merge_sort(list))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
