def OptimizedLinearSearch(numbers, value):
    pass_count = 0
    left = 0
    right = len(numbers) - 1

    while left <= right:
        # Counts the number of passes made
        pass_count += 1
        print(f"PASS {pass_count}: Left = {numbers[left]}, Right = {numbers[right]}")

        # Check from the left side of the array
        if value % 10 == numbers[left] % 10:
            if value == numbers[left]:
                print(f"\n{value} is found at index {left}")
                print(f"Passes made: {pass_count}")
                return True
        
        # Avoids checking the same index if left and right point to the same index
        if left != right: 
            # Check from the right side of the array
            if value % 10 == numbers[right] % 10:
                if value == numbers[right]:
                    print(f"\n{value} is found at index {right}")
                    print(f"Passes made: {pass_count}")
                    return True
                
        left += 1
        right -= 1

    print(f"Passes made: {pass_count}")
    return False

size = int(input("Enter array size: "))
numbers = []

for i in range(size):
    number = int(input(f"Enter value {i + 1}: "))
    numbers.append(number)

while True:
    print("\nArray:", numbers)
    user_input = input("\nEnter number to search (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting search.")
        break
    
    if not user_input.isdigit():
        print("Please enter a valid number or type 'exit'.")
        continue

    value = int(user_input)
    OptimizedLinearSearch(numbers, value)