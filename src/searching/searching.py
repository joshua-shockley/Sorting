# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for item in range(len(arr)):
        if arr[item] == target:
            return item

    return -1   # not found


# arr = [44, 3, 2, 5, 66, -1, 55, 43, 21, 53, 1, 5, 6]
# print("linear", linear_search(arr, 33))
# print("linear", linear_search(arr, -1))

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    for low in range(low, high):
        mid = (low + high) // 2
        if target == arr[mid]:
            # print(arr[target], target)
            return int(arr[target])
        elif target < arr[mid]:
            # print('in the first half of range')
            high = mid - 1
        else:
            # print('in the second half of range')
            low = mid + 1
        return -1  # notfound


# print("binary", binary_search(arr, 33))
# print("binary", binary_search(arr, -1))
# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
