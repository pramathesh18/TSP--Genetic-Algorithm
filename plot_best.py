# Main loop to plot best 3 results from results.txt
import extract
from plot_tsp import plot_route

# Load coordinates
coords = extract.read_tsp("berlin52.tsp")

# Read results.txt and parse distances/routes
results = []
with open("results.txt", "r") as f:
    lines = f.readlines()

for i in range(0, len(lines), 3):  # distance line + route line + blank line
    if i + 1 >= len(lines):
        break
    dist_line = lines[i].strip()
    route_line = lines[i + 1].strip()
    if dist_line.startswith("Final best distance:") and route_line.startswith("Final best route:"):
        distance = float(dist_line.split(":")[1].strip())
        route = eval(route_line.split(":")[1].strip())  # converts string list to Python list
        results.append((distance, route))

# Sort by distance (ascending)
results.sort(key=lambda x: x[0])

# Plot top 3 results
for idx, (dist, route) in enumerate(results[:3], start=1):
    plot_route(coords, route, title=f"Top {idx} TSP Route (Distance={dist:.2f})")
