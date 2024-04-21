def recursiveIteration(arr, i):
    if i >= len(arr):
        return
    print(arr[i])
    i += 1
    recursiveIteration(arr, i)


def arraySliceIteration(arr):
    if len(arr) < 1:
        return
    print(arr)
    arraySliceIteration(arr[:-1])


def iterateArrayThroughPop(arr):
    if len(arr) < 1:
        return
    print(arr.pop(0))
    iterateArrayThroughPop(arr)


arr = [1, 2, 3, 4, 5]

# recursiveIteration(arr, i=0)
# arraySliceIteration(arr)
iterateArrayThroughPop(arr)
