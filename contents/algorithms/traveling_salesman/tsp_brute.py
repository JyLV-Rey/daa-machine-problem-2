from tsp_util import (
    get_city_info,
    get_constraints,
    calculate_route_cost,
    display_results,
    log_passes
)

def generate_permutations(cities, constraints):
    """Generate permutations for TSP where route starts and ends at same city"""
    cities = cities.copy()

    # If start city is specified
    if constraints.get('must_start'):
        start_city = constraints['must_start']
        cities.remove(start_city)
        # Generate all permutations of remaining cities
        from itertools import permutations
        for perm in permutations(cities):
            yield [start_city] + list(perm) + [start_city]
        return

def brute_tsp(cities, distance_matrix, constraints):
    all_routes = []
    best_route = None
    min_cost = float('inf')
    valid_pass_count = 0

    for route in generate_permutations(cities, constraints):
        valid_pass_count += 1
        cost = calculate_route_cost(route, cities, distance_matrix)
        all_routes.append((route, cost))

        if cost < min_cost:
            min_cost = cost
            best_route = route

    log_passes(valid_pass_count, "Brute Force")
    return all_routes, best_route, min_cost

def main():
    print("=== Traveling Salesman Problem Solver (Brute Force) ===")

    # Get city information
    cities, distance_matrix = get_city_info()

    # Get constraints
    constraints = get_constraints(cities)

    # Solve TSP using brute force
    all_routes, best_route, min_cost = brute_tsp(cities, distance_matrix, constraints)

    # Display results
    display_results(all_routes, best_route, min_cost)

if __name__ == "__main__":
    main()
