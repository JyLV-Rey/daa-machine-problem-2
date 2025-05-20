# User input
arrayLength = int(input("Enter length of the array: "))
array = []

print("Enter elements:")
for i in range(arrayLength):
    array.append(int(input(">> ")))

print("Elements:", end=" ")
for i in range(arrayLength):
    print(array[i], end=" ")
print()

# Sorting
for i in range(arrayLength // 2):
    minIndex = maxIndex = i
    didSwap = False # flag for early exit

    for j in range(i + 1, arrayLength - i):
        if array[j] < array[minIndex]:
            minIndex = j
        if array[j] > array[maxIndex]:
            maxIndex = j

    # No swap if element is in the right index
    if minIndex != i:
        array[i], array[minIndex] = array[minIndex], array[i]
        didSwap = True

        if maxIndex == i:
            maxIndex = minIndex

    if maxIndex != arrayLength - i - 1:
        array[arrayLength - i - 1], array[maxIndex] = array[maxIndex], array[arrayLength - i - 1]
        didSwap = True

    if not didSwap:
        print("Remaining part is already sorted. Early exit.\n")
        break

print("Elements:", end=" ")
for i in range(arrayLength):
    print(array[i], end=" ")
print()