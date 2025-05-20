# User input 
array_input = input("Enter array elements separated by commas: ")
array = [int(x.strip()) for x in array_input.split(",")]
arrayLength = len(array)

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
    total_array_accesses += 1  # reading array[minIndex]

    for j in range(x + 1, arrayLength):
        total_array_accesses += 2  # array[j], array[minIndex]
        if array[j] < array[minIndex]:
            minIndex = j
            total_array_accesses += 1  # reading array[minIndex]

    # Swap the current element with the smallest found
    if minIndex != x:
        total_array_accesses += 4  # two reads + two writes
        array[x], array[minIndex] = array[minIndex], array[x]
        total_swaps += 1

    # Show array after each pass
    print(f"After Pass {total_passes}: ", end="")
    for val in array:
        print(val, end=" ")
    print()

# Display the sorted array
print("Sorted Array: ", end = "")
for x in array:
    print(x, end = " ")
print()

# Print counters
print("\nTotal Passes:", total_passes)
print("Total Array Accesses:", total_array_accesses)
print("Total Swaps:", total_swaps)
