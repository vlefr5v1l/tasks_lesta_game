def quicksort(arr):
    if len(arr) <= 1:
        return arr
    m = arr[len(arr) // 2]
    left = [x for x in arr if x < m]
    middle = [x for x in arr if x == m]
    right = [x for x in arr if x > m]
    return quicksort(left) + middle + quicksort(right)
