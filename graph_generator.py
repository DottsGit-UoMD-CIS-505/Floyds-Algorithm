"""
Generates a single graph with a given length

Author: Nicholas Butzke
"""

import random
import networkx as nx
import numpy as np


def generate_graph(n):
    """Create a complete graph (all nodes connected) with random edge weights."""
    graph = nx.complete_graph(n)
    for i, j in graph.edges:
        graph[i][j]["weight"] = random.randint(1, 10)  # Set the maximum cost as needed.

    # Find the minimum spanning tree to ensure connectivity.
    mst = nx.minimum_spanning_tree(graph)

    # Initialize the adjacency matrix with infinity (float('inf')) values.
    adjacency_matrix = np.full((n, n), float("inf"))

    # Fill in the adjacency matrix with edge weights from the minimum spanning tree.
    for i, j in mst.edges:
        weight = mst[i][j]["weight"]
        adjacency_matrix[i][j] = weight
        adjacency_matrix[j][i] = weight

    for i in range(n):
        adjacency_matrix[i][i] = 0

    return adjacency_matrix.tolist()
