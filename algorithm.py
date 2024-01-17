# optimal_path_algorithm.py
import math
from itertools import permutations

def calculate_optimal_route(customers, depot, vehicle_capacity):
    # Create all possible routes using permutations
    all_routes = list(permutations(customers.keys()))

    # Initialize variables to track the best solution
    best_route = None
    best_distance = float("inf")

    # Iterate through all possible routes
    for route in all_routes:
        if route[0] != 1:
            continue  # Start routes from the depot (customer 1)

        current_capacity = 0
        current_route = [1]  # Start with the depot
        current_distance = 0

        for i in range(len(route)):
            customer = route[i]
            demand = customers[customer][2]
            distance = math.sqrt((customers[current_route[-1]][0] - customers[customer][0]) ** 2 +
                                 (customers[current_route[-1]][1] - customers[customer][1]) ** 2)

            if current_capacity + demand <= vehicle_capacity:
                current_route.append(customer)
                current_capacity += demand
                current_distance += distance
            else:
                current_route.append(0)  # Return to the depot
                current_route.append(customer)
                current_capacity = demand
                current_distance += distance

        current_route.append(0)  # Return to the depot
        current_distance += math.sqrt((customers[current_route[-2]][0] - depot[0]) ** 2 +
                                      (customers[current_route[-2]][1] - depot[1]) ** 2)

        if current_distance < best_distance:
            best_distance = current_distance
            best_route = current_route

    return best_route, best_distance
