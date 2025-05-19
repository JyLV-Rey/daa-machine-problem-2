def get_city_info():
    """Get city names and distances between them from the user"""
    cities = []

    # Get city names
    while True:
        city = input("Enter a city name (or 'done' to finish): ").strip()
        if city.lower() == 'done':
            break
        if city in cities:
            print("City already exists. Please enter a different name.")
            continue
        cities.append(city)

    # Initialize distance matrix
    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]

    # Get distances between cities
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            while True:
                try:
                    dist = float(input(f"Enter distance from {cities[i]} to {cities[j]}: "))
                    if dist <= 0:
                        print("Distance must be positive. Please try again.")
                        continue
                    distance_matrix[i][j] = dist
                    distance_matrix[j][i] = dist
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

    return cities, distance_matrix

def get_constraints(cities):
    """Ask user for starting city (which will also be the ending city)"""
    constraints = {
        'must_start': None,
    }

    while True:
        # Ask for starting city
        start = input(f"\nStart and end at which city? ({', '.join(cities)}): ").strip()

        # If empty input, use first city as default
        if not start:
            constraints['must_start'] = cities[0]
            print(f"Using default starting city: {cities[0]}")
            break

        # Check if input is valid
        if start in cities:
            constraints['must_start'] = start
            break
        else:
            print(f"Invalid city. Please choose from: {', '.join(cities)}")

    return constraints

def calculate_route_cost(route, cities, distance_matrix):
    """Calculate total distance for a given route"""
    total = 0
    array_calls = 0
    city_indices = [cities.index(city) for city in route]

    # Sum distances between consecutive cities
    for i in range(len(city_indices) - 1):
        from_idx = city_indices[i]
        to_idx = city_indices[i+1]
        total += distance_matrix[from_idx][to_idx]
        array_calls += 1

    # Add return to starting city
    if len(route) == len(cities) + 1 and route[0] == route[-1]:
        from_idx = city_indices[-1]
        to_idx = city_indices[0]
        total += distance_matrix[from_idx][to_idx]
        array_calls += 1 

    return total, array_calls

def display_results(all_routes, best_route, min_cost, passes=None, algorithm_name=None, runtime=None, total_array_calls=None):
    """Display all valid routes, the optimal one, and optionally pass count"""
    print("\n=== All Valid Routes ===")
    for route, cost in all_routes:
        print(f"{'->'.join(route)} = {cost}")

    print("\n=== Optimal Route ===")
    if best_route:
        print(f"{'->'.join(best_route)} = {min_cost}")
    else:
        print("No valid route found that satisfies the given constraints.")

    # Print passes if provided
    if passes is not None and algorithm_name:
        log_passes(passes, algorithm_name)
    
    # Print runtime and array accesses
    if runtime is not None:
        print(f"\nTotal runtime: {runtime:.6f} seconds")
    if total_array_calls is not None:
        print(f"Total distance matrix accesses: {total_array_calls}")

def log_passes(count, algorithm_name):
    """Print the number of passes for a specific algorithm"""
    print(f"\n{algorithm_name} algorithm evaluated {count} passes")