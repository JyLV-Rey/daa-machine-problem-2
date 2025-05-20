def OptimizedLinearSearch(numbers, value):
    pass_count = 0
    left = 0
    right = len(numbers) - 1

    while left <= right:
        # Counts the number of passes made
        pass_count += 1

        # Check from the left side of the array
        if value % 10 == numbers[left] % 10:
            if value == numbers[left]:
                print(f"{value} is found")
                print(f"Passes made: {pass_count}")
                return True
        
        # Avoids checking the same index if left and right point to the same index
        if left != right: 
            # Check from the right side of the array
            if value % 10 == numbers[right] % 10:
                if value == numbers[right]:
                    print(f"{value} is found")
                    print(f"Passes made: {pass_count}")
                    return True

        left += 1
        right -= 1
    
    print(f"Passes made: {pass_count}")
    return False


numbers = []

for i in range(6):
    number = int(input(f"Enter value {i + 1}: "))
    numbers.append(number)

value = int(input("\nEnter number to search: "))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

if not OptimizedLinearSearch(numbers, value):
    print(f"{value} is not found")