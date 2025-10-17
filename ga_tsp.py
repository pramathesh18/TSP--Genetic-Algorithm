# ga_tsp.py
import random
import extract

def create_route(city_indices):
    route = city_indices[:]
    random.shuffle(route)
    return route

def route_distance(route, dist_matrix):
    total = 0
    for i in range(len(route)):
        total += dist_matrix[route[i]][route[(i + 1) % len(route)]]
    return total

def initial_population(pop_size, city_indices):
    return [create_route(city_indices) for _ in range(pop_size)]

def rank_routes(population, dist_matrix):
    return sorted(population, key=lambda route: route_distance(route, dist_matrix))

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    ptr = 0
    for city in parent2:
        if city not in child:
            while child[ptr] is not None:
                ptr += 1
            child[ptr] = city
    return child

def mutate(route, mutation_rate=0.02):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

def next_generation(current_pop, dist_matrix, elite_size=5, mutation_rate=0.01):
    ranked = rank_routes(current_pop, dist_matrix)
    elites = ranked[:elite_size]
    children = elites[:]
    while len(children) < len(current_pop):
        parent1, parent2 = random.sample(ranked[:20], 2)
        child = crossover(parent1, parent2)
        children.append(mutate(child, mutation_rate))
    return children

def genetic_algorithm(dist_matrix, pop_size=100, generations=1000):
    city_indices = list(range(len(dist_matrix)))
    population = initial_population(pop_size, city_indices)
    
    best_distance = float('inf')
    best_route = None

    for gen in range(generations):
        population = next_generation(population, dist_matrix)
        current_best = rank_routes(population, dist_matrix)[0]
        current_dist = route_distance(current_best, dist_matrix)
        if current_dist < best_distance:
            best_distance = current_dist
            best_route = current_best
        if gen % 50 == 0:
            print(f"Gen {gen}: Best distance = {best_distance:.2f}")

    return best_route, best_distance

if __name__ == "__main__":
    coords = extract.read_tsp("berlin52.tsp")
    dist_matrix = extract.calculate_distance_matrix(coords)
    best_route, best_distance = genetic_algorithm(dist_matrix)
    print("\nFinal best distance:", best_distance)
    print("Best route:", best_route)
