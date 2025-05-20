# User input
array_input = input("Enter array elements separated by commas: ")
array = [int(x.strip()) for x in array_input.split(",")]
arrayLength = len(array)

# Display original array
print("Original Elements:", end=" ")
for i in range(arrayLength):
    print(array[i], end=" ")
print()

# Initialize counters
total_array_accesses = 0
total_passes = 0
total_swaps = 0

# Optimized sorting
for i in range(arrayLength // 2):
    total_passes += 1
    minIndex = maxIndex = i
    didSwap = False

    for j in range(i + 1, arrayLength - i):
        total_array_accesses += 2  # array[j], array[minIndex]
        if array[j] < array[minIndex]:
            minIndex = j
        total_array_accesses += 2  # array[j], array[maxIndex]
        if array[j] > array[maxIndex]:
            maxIndex = j

    if minIndex != i:
        total_array_accesses += 4
        array[i], array[minIndex] = array[minIndex], array[i]
        total_swaps += 1
        didSwap = True
        if maxIndex == i:
            maxIndex = minIndex

    if maxIndex != arrayLength - i - 1:
        total_array_accesses += 4
        array[arrayLength - i - 1], array[maxIndex] = array[maxIndex], array[arrayLength - i - 1]
        total_swaps += 1
        didSwap = True

    # Show array after each pass
    print(f"After Pass {total_passes}: ", end="")
    for val in array:
        print(val, end=" ")
    print()

    if not didSwap:
        print("Remaining part is already sorted. Early exit.\n")
        break

# Display sorted array
print("Sorted Elements:", end=" ")
for i in range(arrayLength):
    print(array[i], end=" ")
print()

# Print counters
print("\nTotal Passes:", total_passes)
print("Total Array Accesses:", total_array_accesses)
print("Total Swaps:", total_swaps)
