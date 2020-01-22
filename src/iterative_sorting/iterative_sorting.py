import random

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        smallest = min(arr[i:])
        #         # TO-DO: find next smallest element
        #         # (hint, can do in 3 loc)
        sml_index = arr.index(smallest)
        # loca1, loca2 = value2, value1 to swap values witout temp storage
        arr[sml_index], arr[i] = arr[i], arr[sml_index]
    return arr


def selection_sort2(arr):
    for i in range(0, len(arr)-1):
        current_i = i
        smlest = current_i
        for nA in range(i+1, len(arr)):
            if arr[nA] < arr[smlest]:  # as passes comparing the new loop to the set previously smallest
                smlest = nA
        # the swap below needs to be assigned under the inner loop so it actually does shit
                arr[current_i], arr[smlest] = arr[smlest], arr[current_i]
                print(arr)
    return arr


the_array = [3, 2, 4, 5, 1, 6, 8, 7, 9, 0]
# selection_sort3(the_array)
# or
# l = list(range(10))
# random.shuffle(l)
# the above creates a random unordered list of numbers 0-9
print("selection", selection_sort2(the_array))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for b in range(i + 1, len(arr)):
            if arr[i] > arr[b]:
                arr[i], arr[b] = arr[b], arr[i]

    return arr


print("bubble", bubble_sort(the_array))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
