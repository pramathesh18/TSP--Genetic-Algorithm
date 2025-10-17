"""

import tsplib95
import math

def load_tsp(filepath):

    Load a TSPLIB .tsp file and return:
      - coords: list of (x, y) tuples
      - dist_matrix: 2D list [ [d_ij], ... ]

    problem = tsplib95.load(filepath)
    coords = [problem.node_coords[node] for node in sorted(problem.get_nodes())]

    # Build distance matrix (Euclidean)
    n = len(coords)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = coords[j]
            dist_matrix[i][j] = round(math.hypot(x1 - x2, y1 - y2))

    return coords, dist_matrix







if __name__ == "__main__":
    filepath = "berlin52.tsp"   # Adjust if your file is elsewhere
    coords, dist_matrix = load_tsp(filepath)

    print(f"Loaded {len(coords)} cities from {filepath}")
    print("First 5 coordinates:", coords[:5])
    print("Distance matrix size:", len(dist_matrix), "x", len(dist_matrix[0]))

    print("\nFirst 5x5 block of distance matrix:")
    for i in range(5):
        print(dist_matrix[i][:5])



        """


# extract.py
import math

def read_tsp(file_path):
    coords = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        start = False
        for line in lines:
            if line.strip() == "NODE_COORD_SECTION":
                start = True
                continue
            if start:
                if line.strip() == "EOF":
                    break
                parts = line.strip().split()
                if len(parts) >= 3:
                    coords.append((float(parts[1]), float(parts[2])))
    return coords

def calculate_distance_matrix(coords):
    n = len(coords)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)
    return dist

if __name__ == "__main__":
    coords = read_tsp("berlin52.tsp")
    distance_matrix = calculate_distance_matrix(coords)
    print(distance_matrix)
