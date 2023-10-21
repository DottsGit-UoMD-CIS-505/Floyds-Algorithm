"""
Main wrapper to test various graphs.
Will generate graphs and print them.
Is able to find the optimal paths in a given graph between 2 vertices.

Author: Nicholas Butzke

P: list[list[int]] = [
    [0, 0, 5, 2, 4, 0, 6],
    [0, 0, 5, 0, 4, 1, 4],
    [2, 0, 0, 2, 4, 2, 4],
    [2, 0, 5, 0, 0, 2, 0],
    [4, 4, 0, 0, 0, 4, 4],
    [7, 7, 7, 7, 7, 0, 0],
    [4, 4, 5, 0, 4, 4, 0],
]
"""

from floyds_algorithm import floyd2
from shortest_path import path
from graph_list_generator import generate_graph_list

GRAPH_VERTICES_QUANTITIES = [5, 10, 25]
GRAPH_QUANTITIES = 10

W_List = generate_graph_list(GRAPH_VERTICES_QUANTITIES, GRAPH_QUANTITIES)

for W in W_List:
    D, P = floyd2(len(W), W)
    print("D Matrix:")
    for row in D:
        for element in row:
            print(f"{int(element):3}", end=" ")
        print()
    print("-------------------------------------")
    print("P Matrix:")
    for row in P:
        for element in row:
            print(f"{element:3}", end=" ")
        print()
    print("-------------------------------------")
    print("-------------------------------------")
    if W == W_List[0]:
        P_Classic = P

START = 7
FINISH = 3
print(f"Optimal path from v{START} to v{FINISH}:")
print(f"v{START}", end=" -> ")
path(P_Classic, START - 1, FINISH - 1)
print(f"v{FINISH}", end="")
