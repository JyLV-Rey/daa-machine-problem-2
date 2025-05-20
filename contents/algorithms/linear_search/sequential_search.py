def linear_search(arr, key):
    passes = 0  
    for index in range(len(arr)):
        passes += 1
        if arr[index] == key:
            print(f"Element found at index {index}")
            print(f"Total Passes: {passes}")
            return
    print("Element not found in the array.")
    print(f"Total Passes: {passes}")

# Initial array input
size = int(input("Enter the size of the array: "))

arr = []
print("Enter the elements of the array:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

while True:
    print("\nArray:", arr)
    user_input = input("\nEnter number to search (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting search.")
        break

    if not user_input.isdigit():
        print("Please enter a valid number or type 'exit'.")
        continue

    key = int(user_input)
    linear_search(arr, key)