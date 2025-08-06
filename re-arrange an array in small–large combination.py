def rearrange_small_large(arr):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    result = []
    left = 0
    right = len(arr) - 1


    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1

    return result


arr = [1, 3, 5, 2, 8, 7, 4]
print("Re-arranged array:", rearrange_small_large(arr))
