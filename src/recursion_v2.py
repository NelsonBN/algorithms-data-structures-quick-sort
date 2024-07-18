def quick_sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return


    i = left

    for j in range(left, right):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    pivot = i


    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)



array = [5, 3, 21, 13, 1, 7, 6, 3]
print("Before: ", array)

quick_sort(array)

print("After: ", array)
