# User input 
print("Enter the length of the array: ", end = "")
arrayLength = int(input()) # Read the length of the array
array = []

# Prompt the user to enter the array length
print("Enter element: ")
for x in range(arrayLength):
    print(">> ", end = "")
    array.append(int(input()))

# Display the array before sorting
print("Array: ", end = "")
for x in array:
    print(x, end = " ")
print()

# Initialize counters
total_passes = 0
total_array_accesses = 0
total_swaps = 0

# Sorting
for x in range(arrayLength - 1):
    total_passes += 1
    minIndex = x
    # Access for initial minIndex element
    total_array_accesses += 1  # reading array[minIndex]

    for j in range(x + 1, arrayLength):
        # Each comparison reads two elements
        total_array_accesses += 2  # array[j], array[minIndex]
        if array[j] < array[minIndex]:
            minIndex = j
            # Access for new minIndex element
            total_array_accesses += 1  # reading array[minIndex]

    # Swap the current element with the smallest found
    if minIndex != x:
        # 4 accesses: two reads + two writes
        total_array_accesses += 4
        temp = array[x]
        array[x] = array[minIndex]
        array[minIndex] = temp
        total_swaps += 1

# Display the sorted array
print("Sorted Array: ", end = "")
for x in array:
    print(x, end = " ")
print()

# Print counters
print("\nTotal Passes:", total_passes)
print("Total Array Accesses:", total_array_accesses)
print("Total Swaps:", total_swaps)
