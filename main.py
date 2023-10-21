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
import time

from networkx import shortest_path
from floyds_algorithm import floyd2
from shortest_path import path
from graph_list_generator import generate_graph_list
from log_output import log_output

GRAPH_VERTICES_QUANTITIES = [5, 10, 25, 50, 100]
GRAPH_QUANTITIES = 10

W_List = generate_graph_list(GRAPH_VERTICES_QUANTITIES, GRAPH_QUANTITIES)
with open("output.txt", "w", encoding="utf-8") as file:
    runtimes = []
    for W in W_List:
        start_time = time.time()
        D, P = floyd2(len(W), W)
        end_time = time.time()

        log_output(f"Runtime: {end_time - start_time}s", file)
        runtimes.append(end_time - start_time)

        log_output("D Matrix:", file)
        for row in D:
            for element in row:
                log_output(f"{int(element):3}", file, " ")
            log_output("", file)

        log_output("-------------------------------------", file)
        log_output("P Matrix:", file)
        for row in P:
            for element in row:
                log_output(f"{element:3}", file, " ")
            log_output("", file)
        log_output("-------------------------------------", file)
        log_output("-------------------------------------", file)
        if W == W_List[0]:
            P_Classic = P
    previous_node_count = len(W_List[0])
    cycle_total_runtime = 0
    for i, runtime in enumerate(runtimes):
        if previous_node_count != len(W_List[i]):
            log_output(
                f"Node count: {previous_node_count:3} | Average runtime: {cycle_total_runtime/len(W_List[i])}s",
                file,
            )
        log_output(f"Node count: {len(W_List[i]):3} | {runtime}s", file)
        previous_node_count = len(W_List[i])
        cycle_total_runtime += runtime
    log_output(
        f"Node count: {previous_node_count:3} | Average runtime: {cycle_total_runtime/len(W_List[i])}s",
        file,
    )

    START = 7
    FINISH = 3
    log_output(f"Optimal path from v{START} to v{FINISH}:", file)
    log_output(f"v{START}", file, " -> ")
    path(P_Classic, START - 1, FINISH - 1, file)
    log_output(f"v{FINISH}", file, "")
