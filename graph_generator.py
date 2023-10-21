"""
Generates a single graph with a given length

Author: Nicholas Butzke
"""

import random
import networkx as nx
import numpy as np


def generate_graph(n):
    """Create a connected graph with random edge weights."""
    graph = nx.complete_graph(n)
    for i, j in graph.edges:
        graph[i][j]["weight"] = random.randint(1, 10)

    # Find the minimum spanning tree to ensure connectivity
    mst = nx.minimum_spanning_tree(graph)

    # Use infinity to mean unconnected instead of 0
    adjacency_matrix = np.full((n, n), float("inf"))

    # Fill in the adjacency matrix with edge weights from the minimum spanning tree.
    for i, j in mst.edges:
        weight = mst[i][j]["weight"]
        adjacency_matrix[i][j] = weight
        adjacency_matrix[j][i] = weight

    # Make nodes' self reference cost be zero
    for i in range(n):
        adjacency_matrix[i][i] = 0

    return adjacency_matrix.tolist()
