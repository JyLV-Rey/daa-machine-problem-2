def brute_force_knapsack(weights, values, capacity):
    n = len(weights)
    total_subsets = 2 ** n
    print("\nTotal subsets to evaluate:", total_subsets)

    max_value = 0
    best_items = []
    all_subsets = []

    comparisons = 0
    array_accesses = 0

    # Try all combinations
    for i in range(total_subsets):
        temp_items = []
        total_weight = 0
        total_value = 0

        for j in range(n):
            if (i >> j) & 1:
                temp_items.append(j)
                total_weight += weights[j]
                total_value += values[j]
                array_accesses += 2  # weights[j], values[j]

        valid = total_weight <= capacity
        comparisons += 1  # for this validity check
        all_subsets.append([temp_items, total_weight, total_value, valid])

        comparisons += 1  # for total_value > max_value
        if valid and total_value > max_value:
            max_value = total_value
            best_items = temp_items

    return max_value, best_items, all_subsets, comparisons, array_accesses


def main():
    capacity = int(input("Max weight capacity: "))
    n = int(input("How many items? "))

    weights = []
    values = []

    print("\nEnter weight and value for each item:")
    for i in range(n):
        print(f"Item {i+1}:")
        w = int(input("  Weight: "))
        v = int(input("  Value: "))
        weights.append(w)
        values.append(v)

    max_value, best_items, all_subsets, comparisons, array_accesses = brute_force_knapsack(weights, values, capacity)

    print("\n>>> Best Combination <<<")
    print("Items to include:", [i+1 for i in best_items])
    print("Total weight:", sum(weights[i] for i in best_items))
    print("Total value:", max_value)
    print("Total comparisons:", comparisons)
    print("Total array accesses:", array_accesses)

    print("\n>>> All Subsets <<<")
    for i, subset in enumerate(all_subsets):
        items, w, v, valid = subset
        print(f"Subset {i+1}: Items {[x+1 for x in items]}, Weight = {w}, Value = {v}", end=" ")
        if valid:
            print("- Valid")
        else:
            print("- Invalid (too heavy)")


if __name__ == "__main__":
    main()
