A = [64, 25, 12, 22, 11]


def selectionSort(arr):
    unsorted_arr = arr
    arr_length = len(unsorted_arr)
    for i in range(arr_length):
        min_idx = 1
        for j in range(i + 1, arr_length):
            if unsorted_arr[min_idx] > unsorted_arr[j]:
                min_idx = j
        unsorted_arr[min_idx], unsorted_arr[i] = unsorted_arr[i], unsorted_arr[min_idx]
    return unsorted_arr


res = selectionSort(A)
print(f"Sorted Array: {res}")
