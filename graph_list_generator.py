"""
Generates a list of initial graphs to be evaluated by Flody's Algorithm.

Author: Nicholas Butzke
"""
from math import inf
from graph_generator import generate_graph


def generate_graph_list(graph_lengths, graph_quantity: int = 1):
    """Calls graph generator multiple times to generate multiple graphs.
    Also uses custom graphs."""

    # Custom Graphs
    # w_1 is the graph from the HW
    w_1: list[list[int]] = [
        [0, 4, inf, inf, inf, 10, inf],
        [3, 0, inf, 18, inf, inf, inf],
        [inf, 6, 0, inf, inf, inf, inf],
        [inf, 5, 15, 0, 2, 19, 5],
        [inf, inf, 12, 1, 0, inf, inf],
        [inf, inf, inf, inf, inf, 0, 10],
        [inf, inf, inf, 8, inf, inf, 0],
    ]

    # w_2 is the graph from the HW that forces it into a long path
    w_2: list[list[int]] = [
        [0, 4, inf, inf, inf, 10, inf],
        [3, 0, inf, 18, inf, inf, inf],
        [inf, 6, 0, inf, inf, inf, inf],
        [inf, 500, 15, 0, 2, 190, 5],
        [inf, inf, 12, 1, 0, inf, inf],
        [inf, inf, inf, inf, inf, 0, 10],
        [inf, inf, inf, 8, inf, inf, 0],
    ]

    # Add the custom graphs to the graph list
    graph_list: list[list[list[int]]] = []
    graph_list.append(w_1)
    graph_list.append(w_2)

    # Generate new graphs with the given parameters and add them to the list
    for n in graph_lengths:
        for _ in range(graph_quantity):
            graph_list.append(generate_graph(n))
    return graph_list
