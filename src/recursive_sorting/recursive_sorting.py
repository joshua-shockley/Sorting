# TO-DO: complete the helpe function below to merge 2 sorted arrays
import random


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, len(merged_arr)-1):
        left = len(merged_arr)-len(arrB)
        print(left)
        smallA = min(arrA[i:])
        smallA_index = arrA.index(smallA)
        arrA[smallA_index], merged_arr[i] = merged_arr[i], arrA[smallA_index]
        print("after arrA", merged_arr)
        # result = merged_arr
        smallB = min(arrB[i:])
        smallB_index = arrB.index(smallB)
        arrB[smallB_index], merged_arr[
            i+left] = merged_arr[i+left], arrB[smallB_index]
        print(" after arrB", merged_arr)
        # result = merged_arr
        # return result
    # print("line 23", result)
    # return merged_arr


l = list(range(10))
m = list(range(10, 20))
print(l, m)
print(merge(l, m))
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


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
