# User input
arrayLength = int(input("Enter length of the array: "))
array = []

print("Enter elements:")
for i in range(arrayLength):
    array.append(int(input(">> ")))  # Read each element

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
    didSwap = False  # Flag for early termination

    # Find the indexes of the minimum and maximum elements in the unsorted portion
    for j in range(i + 1, arrayLength - i):
        # Access for comparison
        total_array_accesses += 2  # array[j], array[minIndex]
        if array[j] < array[minIndex]:
            minIndex = j
        # Access for comparison
        total_array_accesses += 2  # array[j], array[maxIndex]
        if array[j] > array[maxIndex]:
            maxIndex = j

    # Swap the minimum element to the front
    if minIndex != i:
        # 4 accesses: two reads and two writes during swap
        total_array_accesses += 4
        array[i], array[minIndex] = array[minIndex], array[i]
        total_swaps += 1
        didSwap = True

        # If the max element was originally at index i, its position has now changed due to swap
        if maxIndex == i:
            maxIndex = minIndex

    # Swap the maximum element to the end
    if maxIndex != arrayLength - i - 1:
        # 4 accesses: two reads and two writes during swap
        total_array_accesses += 4
        array[arrayLength - i - 1], array[maxIndex] = array[maxIndex], array[arrayLength - i - 1]
        total_swaps += 1
        didSwap = True

    # If no swap occurred during this pass, array is already sorted
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
