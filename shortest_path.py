"""
Evaluates the shortest path between two nodes for a given P graph.

Author: Nicholas Butzke
"""

from log_output import log_output


def path(P, q: int, r: int, file):
    """Print the intermediate vertices on a shortest path from
    one vertex to another vertex in a weighted graph."""
    shortest_path = []
    if P[q][r] != 0:
        path(P, q, P[q][r] - 1, file)
        log_output(f"v{P[q][r]}", file, " -> ")
        # print(f"v{P[q][r]}", end=" -> ")
        path(P, P[q][r] - 1, r, file)
    return shortest_path
