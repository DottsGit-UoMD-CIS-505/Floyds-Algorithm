from floyds_algorithm import floyd2
from shortest_path import path
from math import inf

W: list[list[int]] = [
    [0, 4, inf, inf, inf, 10, inf],
    [3, 0, inf, 18, inf, inf, inf],
    [inf, 6, 0, inf, inf, inf, inf],
    [inf, 5, 15, 0, 2, 19, 5],
    [inf, inf, 12, 1, 0, inf, inf],
    [inf, inf, inf, inf, inf, 0, 10],
    [inf, inf, inf, 8, inf, inf, 0],
]

D, P = floyd2(7, W)
print("D Matrix:")
for row in D:
    for element in row:
        print(f"{element:2}", end=" ")
    print()
print("-------------------------------------")
print("P Matrix:")
for row in P:
    for element in row:
        print(f"{element:2}", end=" ")
    print()

"""
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

start = 7
finish = 3
print(f"Optimal path from v{start} to v{finish}:")
print(f"v{start}", end=" -> ")
path(P, start - 1, finish - 1)
print(f"v{finish}", end="")
