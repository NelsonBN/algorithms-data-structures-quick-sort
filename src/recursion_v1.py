def quick_sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i



array = [5, 3, 21, 13, 1, 7, 6, 3]
print("Before: ", array)

quick_sort(array)

print("After: ", array)
