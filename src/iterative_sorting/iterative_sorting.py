import random
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]

list = [0, 2, 5, 1, 3, 6, 4, 9, 7, 8, 10]
print("on line 4", list)

# TO-DO: Complete the selection_sort() function below


# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr)):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)

#         # another loop of range +1 of other loop to compare the indicies and swap if i is smaller
#         for n in range(i+1, len(arr)):
#             if arr[n] < arr[smallest_index]:
#                 arr[smallest_index], arr[n] = arr[n], arr[smallest_index]

#         # TO-DO: swap

#     return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # og = arr.copy()
    # print(f'starting point\n', arr)
    while True:  # keeping true until at end with count=0
        count = 0
        if len(arr) <=1:
            return arr
        else:
            for i in range(1, len(arr)):
                # print(f'just inside main loop\n')
                # print('the count before evaluating', count)
                # print(arr[i-1], arr[i])
                if arr[i] < arr[i-1]:
                    # print('before making swap', count)
                    # print(arr[i-1], arr[i])
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    # print(arr[i-1], arr[i])
                    count += 1
                    # print('after swap', count)
                elif i == len(arr)-1 and count == 0:
                    # print("copy original list", og)
                    # print("result bubble sort", arr)
                    return arr
    return False


print(bubble_sort(list))
print('arr1', arr1)
print(bubble_sort(arr1))
print('arr2', arr2)
print(bubble_sort(arr2))
print('arr3', arr3)
print(bubble_sort(arr3))
# print(bubble_sort(arr4))

# STRETCH: implement the Count Sort function below


# def count_sort(arr, maximum=-1):

#     return arr
