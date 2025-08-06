def frequency_descending(arr):
    freq = []

    # Step 1: Count frequencies manually
    for i in range(len(arr)):
        found = False
        for j in range(len(freq)):
            if freq[j][0] == arr[i]:
                freq[j][1] += 1
                found = True
                break
        if not found:
            freq.append([arr[i], 1])

    # Step 2: Sort by frequency (descending)
    for i in range(len(freq)):
        for j in range(i + 1, len(freq)):
            if freq[i][1] < freq[j][1]:
                freq[i], freq[j] = freq[j], freq[i]

    # Step 3: Print the result
    for pair in freq:
        print(pair[0], ":", pair[1])


# Sample input
arr = [50, 20, 150, 20, 50, 10, 30, 10, 10]
frequency_descending(arr)
