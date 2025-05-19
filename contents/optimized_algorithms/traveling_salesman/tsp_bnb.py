import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from contents.algorithms.traveling_salesman.tsp_util import (
    get_city_info,
    get_constraints,
    display_results,
    log_passes
)   

def branch_and_bound_tsp(cities, distance_matrix, constraints):
    best_route = None
    min_cost = float('inf')
    valid_pass_count = 0
    all_routes = []

    # Handle constraints
    start_city = constraints.get('must_start', cities[0])
    remaining_cities = [c for c in cities if c != start_city]

    def backtrack(current_route, current_cost, remaining_cities):
        nonlocal best_route, min_cost, valid_pass_count, all_routes

        # Base case: all cities visited, return to start
        if not remaining_cities:
            final_cost = current_cost + distance_matrix[cities.index(current_route[-1])][cities.index(start_city)]
            final_route = current_route + [start_city]

            all_routes.append((final_route, final_cost))
            valid_pass_count += 1

            if final_cost < min_cost:
                min_cost = final_cost
                best_route = final_route
            return

        # Explore all possibilities with pruning
        for next_city in remaining_cities:
            # Calculate new cost
            last_city = current_route[-1]
            new_cost = current_cost + distance_matrix[cities.index(last_city)][cities.index(next_city)]

            # Prune if this path can't possibly be better
            if new_cost >= min_cost:
                continue

            # Recursive call
            backtrack(
                current_route + [next_city],
                new_cost,
                [c for c in remaining_cities if c != next_city]
            )

    # Start backtracking from the starting city
    backtrack([start_city], 0, remaining_cities)

    log_passes(valid_pass_count, "Branch and Bound")
    return all_routes, best_route, min_cost

def main():
    print("=== Traveling Salesman Problem Solver (Branch and Bound - Hamiltonian Cycle) ===")

    # Get city information
    cities, distance_matrix = get_city_info()

    # Get constraints
    constraints = get_constraints(cities)

    # Solve TSP using branch and bound
    all_routes, best_route, min_cost = branch_and_bound_tsp(cities, distance_matrix, constraints)

    # Display results
    display_results(all_routes, best_route, min_cost)

if __name__ == "__main__":
    main()
