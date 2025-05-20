from tsp_util import (
    get_city_info,
    get_constraints,
    calculate_route_cost,
    display_results,
    log_passes
)
import time

def generate_permutations(cities, constraints):
    """Generate permutations for TSP where route starts and ends at the same city"""
    cities = cities.copy()

    # If start city is specified
    if constraints.get('must_start'):
        start_city = constraints['must_start']
        cities.remove(start_city)

        # Generate all permutations of remaining cities
        for perm in permute(cities):
            yield [start_city] + list(perm) + [start_city]
        return

def permute(cities):
    """Generate all permutations of the list of cities using recursion."""
    # Base case: if no cities left, yield empty list
    if len(cities) == 0:
        yield []
    else:
        for i in range(len(cities)):
            city = cities[i]
            remaining_cities = cities[:i] + cities[i+1:]
            for perm in permute(remaining_cities):
                yield [city] + perm

def brute_tsp(cities, distance_matrix, constraints):
    """Brute force TSP solver evaluating all possible routes"""
    all_routes = []
    best_route = None
    min_cost = float('inf')
    valid_pass_count = 0
    total_array_calls = 0

    # Evaluate each generated route permutation
    for route in generate_permutations(cities, constraints):
        valid_pass_count += 1
        cost, array_calls = calculate_route_cost(route, cities, distance_matrix)
        total_array_calls += array_calls
        all_routes.append((route, cost))

        # Update best route if cheaper found
        if cost < min_cost:
            min_cost = cost
            best_route = route

    log_passes(valid_pass_count, "Brute Force")
    return all_routes, best_route, min_cost, total_array_calls

def main():
    print("=== Traveling Salesman Problem Solver (Brute Force) ===")

    # Get city information
    cities, distance_matrix = get_city_info()

    # Get constraints
    constraints = get_constraints(cities)

    # Solve TSP using brute force
    start_time = time.perf_counter()
    all_routes, best_route, min_cost, array_calls = brute_tsp(cities, distance_matrix, constraints)
    runtime = time.perf_counter() - start_time

    # Display results
    display_results(all_routes, best_route, min_cost, runtime=runtime, total_array_calls=array_calls)

if __name__ == "__main__":
    main()