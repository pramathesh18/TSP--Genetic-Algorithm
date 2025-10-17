
import random
import time
import extract


def route_distance(route, dist_matrix):
    total = 0.0
    n = len(route)
    for i in range(n):
        a = route[i]
        b = route[(i + 1) % n]
        total += dist_matrix[a][b]
    return total

def initial_population(pop_size, city_indices):
    return [random.sample(city_indices, len(city_indices)) for _ in range(pop_size)]

def rank_population(population, dist_matrix):
    distances = [route_distance(r, dist_matrix) for r in population]
    paired = list(zip(population, distances))
    paired.sort(key=lambda x: x[1])
    return [p[0] for p in paired], [p[1] for p in paired]

def tournament_select(population, distances, k=5):
    n = len(population)
    best_idx = None
    best_dist = float('inf')
    for _ in range(k):
        i = random.randrange(n)
        d = distances[i]
        if d < best_dist:
            best_dist = d
            best_idx = i
    return population[best_idx]

def ordered_crossover(parent1, parent2):
    size = len(parent1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[a:b+1] = parent1[a:b+1]
    p2_idx = 0
    for i in range(size):
        if child[i] is None:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
    return child

def swap_mutation(route, mutation_rate=0.02):
    n = len(route)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randrange(n)
            route[i], route[j] = route[j], route[i]
    return route

def inversion_mutation(route, mutation_rate=0.02):
    if random.random() < mutation_rate:
        a, b = sorted(random.sample(range(len(route)), 2))
        route[a:b+1] = reversed(route[a:b+1])
    return route



def genetic_algorithm(
    dist_matrix,
    pop_size=500,
    generations=2000,
    elite_size=40,
    tournament_k=5,
    mutation_rate=0.04,
    crossover_rate=0.9,
    use_inversion_mutation=False,
    seed=42
):
    random.seed(seed)
    city_indices = list(range(len(dist_matrix)))
    population = initial_population(pop_size, city_indices)
    ranked_pop, ranked_dists = rank_population(population, dist_matrix)

    best_route = ranked_pop[0][:]
    best_distance = ranked_dists[0]

    print(f"Start: pop_size={pop_size}, gens={generations}, elites={elite_size}, tourn_k={tournament_k}, mut_rate={mutation_rate}, cross_rate={crossover_rate}")

    start_time = time.time()

    for gen in range(1, generations + 1):
        new_population = []

 
        elites = [r[:] for r in ranked_pop[:elite_size]]
        new_population.extend(elites)

   
        while len(new_population) < pop_size:
            parent1 = tournament_select(ranked_pop, ranked_dists, k=tournament_k)
            parent2 = tournament_select(ranked_pop, ranked_dists, k=tournament_k)
            if random.random() < crossover_rate:
                child = ordered_crossover(parent1, parent2)
            else:
                child = parent1[:]
            if use_inversion_mutation:
                child = inversion_mutation(child, mutation_rate)
            else:
                child = swap_mutation(child, mutation_rate)
            new_population.append(child)

        ranked_pop, ranked_dists = rank_population(new_population, dist_matrix)
        gen_best_route = ranked_pop[0]
        gen_best_dist = ranked_dists[0]

        if gen_best_dist < best_distance:
            best_distance = gen_best_dist
            best_route = gen_best_route[:]

        elapsed = time.time() - start_time
        print(f"Gen {gen}/{generations}  GenBest={gen_best_dist:.2f}  GlobalBest={best_distance:.2f}  Elapsed={elapsed:.1f}s")

    return best_route, best_distance


if __name__ == "__main__":
   
    coords = extract.read_tsp("berlin52.tsp")
    dist_matrix = extract.calculate_distance_matrix(coords)

 
    POP_SIZE = 500
    GENERATIONS = 2000
    ELITE_SIZE = 40
    TOURN_K = 7
    MUT_RATE = 0.03
    CROSS_RATE = 0.9
    USE_INVERSION = True  

    with open("results.txt", "a") as file:
        for i in range(3210, 3220):
            best_route, best_dist = genetic_algorithm(
                dist_matrix,
                pop_size=POP_SIZE,
                generations=GENERATIONS,
                elite_size=ELITE_SIZE,
                tournament_k=TOURN_K,
                mutation_rate=MUT_RATE,
                crossover_rate=CROSS_RATE,
                use_inversion_mutation=USE_INVERSION,
                seed = i*i +i+52
            )

            if(best_dist < 8000):
                file.write(f"Final best distance: {best_dist}\n")
                file.write(f"Final best route: {best_route}\n\n")

    print("\nFinal best distance:", best_dist)
    print("Final best route:", best_route)
        