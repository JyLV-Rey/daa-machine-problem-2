# User input 
print("Enter the length of the array: ", end = "")
arrayLength = int(input())
array = []

print("Enter element: ")
for x in range (arrayLength):
    print(">> ", end = "")
    array.append(int(input()))

print("Array: ", end = "")
for x in array:
    print(x, end = " ")

# Sorting
for x in range(arrayLength-1):
    minIndex = x
    for j in range (x+1, arrayLength):
        if array[j] < minIndex:
            minIndex = j
    temp = array[x]
    array[x] = array[minIndex]
    array[minIndex] = temp

print("\nSorted Array: ", end = "")
for x in array:
    print(x, end = " ")