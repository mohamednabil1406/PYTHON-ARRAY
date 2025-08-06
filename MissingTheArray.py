def find_missing_number(arr):
    n = len(arr) + 1  # Total numbers from 1 to n
    expected_sum = 0
    for i in range(1, n + 1):  # instead of use sum(arr)
        expected_sum += i

    actual_sum = 0
    for i in range(len(arr)):
        actual_sum += arr[i]

    missing_number = expected_sum - actual_sum
    return missing_number

# Example input
arr = [3, 7, 1, 2, 8, 4, 5]
print("Missing number is:", find_missing_number(arr))
