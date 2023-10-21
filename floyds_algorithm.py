"""
Computes floyds algorithm with a given weight graph

Author: Nicholas Butzke
"""


def floyd2(n: int, W: list[list[int]]):
    """Finds the costs and shortest path from each vertext to every other vertex"""
    i: int = 1
    j: int = 1
    k: int = 1
    D: list[list[int]]
    P: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    P[i][j] = k + 1
                    D[i][j] = D[i][k] + D[k][j]
    return D, P
