def sequential_search(arr, key):
    passes = 0  
    for index in range(len(arr)):
        passes += 1
        if arr[index] == key:
            return index, passes
    return False, passes

size = int(input("Enter the size of the array: "))

arr = []
print("Enter the elements of the array:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

key = int(input("Enter the element to search for: "))

result, passes = sequential_search(arr, key)

if result != False:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array.")

print(f"Total Passes: {passes}")




