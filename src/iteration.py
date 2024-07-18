def quick_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    stack = [(0, n - 1)]

    while stack:
        left, right = stack.pop()

        pivot = partition(arr, left, right)

        if left < pivot - 1:
            stack.append((left, pivot - 1))

        if pivot + 1 < right:
            stack.append((pivot + 1, right))


def partition(arr, left, right):
    i = left

    for j in range(left, right):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i



array = [5, 3, 21, 13, 1, 7, 6, 3]
print("Before: ", array)

quick_sort(array)

print("After: ", array)
