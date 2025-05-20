# Node class with path tracking
class Node:
    def __init__(self, level, value, weight, bound, path):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.path = path[:]  # Boolean list: True if item is taken

# Function to calculate upper bound
def calculate_bound(node, n, capacity, values, weights):
    if node.weight >= capacity:
        return 0

    bound = node.value
    total_weight = node.weight
    i = node.level + 1

    while i < n and total_weight + weights[i] <= capacity:
        total_weight += weights[i]
        bound += values[i]
        i += 1

    if i < n:
        remain = capacity - total_weight
        bound += (values[i] / weights[i]) * remain

    return bound

# Branch and Bound knapsack solver
def knapsack_branch_and_bound(values, weights, capacity, original_indices):
    n = len(values)
    max_value = 0
    best_path = []
    queue = []

    root = Node(-1, 0, 0, 0, [])
    root.bound = calculate_bound(root, n, capacity, values, weights)
    queue.append(root)

    while queue:
        node = queue.pop(0)

        if node.level == n - 1 or node.bound <= max_value:
            continue

        next_level = node.level + 1

        # Include the item
        include_path = node.path + [True]
        include = Node(
            next_level,
            node.value + values[next_level],
            node.weight + weights[next_level],
            0,
            include_path
        )
        include.bound = calculate_bound(include, n, capacity, values, weights)

        if include.weight <= capacity and include.value > max_value:
            max_value = include.value
            best_path = include.path

        if include.bound > max_value:
            queue.append(include)

        # Exclude the item
        exclude_path = node.path + [False]
        exclude = Node(
            next_level,
            node.value,
            node.weight,
            0,
            exclude_path
        )
        exclude.bound = calculate_bound(exclude, n, capacity, values, weights)

        if exclude.bound > max_value:
            queue.append(exclude)

    selected_items = []
    total_weight = 0
    for i, taken in enumerate(best_path):
        if taken:
            selected_items.append(original_indices[i])
            total_weight += weights[i]

    return max_value, selected_items, total_weight

# ========== INPUT VALIDATION ==========
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid non-negative integer.")

def get_item_input(index):
    print(f"\nItem {index + 1}:")
    value = get_positive_integer("  Enter value: ")
    weight = get_positive_integer("  Enter weight: ")
    return value, weight

# ========== MAIN ==========
print("Knapsack Problem Solver using Branch and Bound\n")

num_items = get_positive_integer("Enter number of items: ")

values = []
weights = []
original_indices = list(range(num_items))  # Track original item index

for i in range(num_items):
    value, weight = get_item_input(i)
    values.append(value)
    weights.append(weight)

capacity = get_positive_integer("\nEnter knapsack capacity: ")

# Sort by value/weight ratio and keep original index mapping
for i in range(num_items):
    for j in range(i + 1, num_items):
        ratio_i = values[i] / weights[i] if weights[i] != 0 else 0
        ratio_j = values[j] / weights[j] if weights[j] != 0 else 0
        if ratio_i < ratio_j:
            values[i], values[j] = values[j], values[i]
            weights[i], weights[j] = weights[j], weights[i]
            original_indices[i], original_indices[j] = original_indices[j], original_indices[i]

# Solve the problem
max_value, selected_items, total_weight = knapsack_branch_and_bound(values, weights, capacity, original_indices)

# Output
print(f"\nMaximum value in the knapsack: {max_value}")
print(f"Items included (original indices starting at 0): {sorted(selected_items)}")
print(f"Total weight used: {total_weight} / {capacity}")
