def remove_duplicates(arr):
    result = []
    for i in range(len(arr)):
        duplicate = False
        # Check if arr[i] is already in result
        for j in range(len(result)):
            if arr[i] == result[j]:
                duplicate = True
                break
        if not duplicate:
            result.append(arr[i])
    return result

# Sample input
arr = [1, 2, 2, 3, 4, 4, 5]
print("Array after removing duplicates:", remove_duplicates(arr))
