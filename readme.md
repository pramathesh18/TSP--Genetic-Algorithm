# TSP Genetic Algorithm (Berlin52)

Small project implementing Genetic Algorithms for the Traveling Salesman Problem using the TSPLIB `berlin52.tsp`.

Files
- [berlin52.tsp](berlin52.tsp) — TSPLIB instance of 52 cities
- [extract.py](extract.py) — data loader: [`extract.read_tsp`](extract.py), [`extract.calculate_distance_matrix`](extract.py)
- [run_ga.py](run_ga.py) — main GA runner using tournament selection and elitism: [`run_ga.genetic_algorithm`](run_ga.py)
- [ga_tsp1.py](ga_tsp1.py) — alternate runner with same GA implementation: [`ga_tsp1.genetic_algorithm`](ga_tsp1.py)
- [ga_tsp.py](ga_tsp.py) — simpler GA implementation: [`ga_tsp.genetic_algorithm`](ga_tsp.py)
- [plot_tsp.py](plot_tsp.py) — plotting helper: [`plot_tsp.plot_route`](plot_tsp.py)
- [plot_best.py](plot_best.py) — parse [results.txt](results.txt) and plot top routes using [`plot_tsp.plot_route`](plot_tsp.py)
- [results.txt](results.txt) — generated GA output (ignored by default)

Requirements
- Python 3.8+
- See `requirements.txt`  



Notes and tips
- `extract.read_tsp` reads coordinates from [berlin52.tsp](berlin52.tsp) and `extract.calculate_distance_matrix` builds the distance matrix.
- `results.txt` is appended by runs; it can be large. It's included in `.gitignore` by default in this repo template.
- Tweak GA parameters in `run_ga.py` and `ga_tsp1.py` (population size, generations, mutation rate, elite size).


```