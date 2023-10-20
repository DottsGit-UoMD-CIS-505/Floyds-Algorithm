def path(P, q: int, r: int):
    """Print the intermediate vertices on a shortest path from
    one vertex to another vertex in a weighted graph."""
    if P[q][r] != 0:
        path(P, q, P[q][r] - 1)
        print(f"v{P[q][r]}", end=" -> ")
        path(P, P[q][r] - 1, r)
