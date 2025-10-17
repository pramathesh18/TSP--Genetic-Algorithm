# plot_tsp_route.py
import matplotlib.pyplot as plt

def plot_route(coords, route, title="TSP Route"):
    """
    coords : list of tuples [(x1, y1), (x2, y2), ...]
    route  : list of indices defining the order of visiting cities
    """
    # Reorder coordinates according to route
    route_coords = [coords[i] for i in route]
    # Append first city at the end to close the tour
    route_coords.append(route_coords[0])

    xs, ys = zip(*route_coords)

    plt.figure(figsize=(10, 8))
    plt.plot(xs, ys, 'o-', color='blue', markersize=8, linewidth=2)
    plt.scatter(xs[0], ys[0], color='red', s=100, label="Start/End")
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    import extract
    # Load your coordinates
    coords = extract.read_tsp("berlin52.tsp")
    
    # Example route (replace with GA output)
    best_route = list(range(len(coords)))  # identity order for example
    
    plot_route(coords, best_route, title="Example TSP Route")
