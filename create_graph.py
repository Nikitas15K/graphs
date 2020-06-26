import community
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import igraph
import time
import numpy as np

    # Each element of the list must be of the form `(n, m,
    #         d)`, where `n` is the number of nodes in the shell, `m` is
    #         the number of edges in the shell, and `d` is the ratio of
    #         inter-shell (next) edges to intra-shell edges. If `d` is zero,
    #         there will be no intra-shell edges, and if `d` is one there
    #         will be all possible intra-shell edges
constructor = [(10, 20, 0.8), (20, 40, 0.8)]
Graph1 = nx.random_shell_graph(constructor)
nx.draw(Graph1, edge_labels=True)
plt.show()
nx.write_gml(Graph1, "C:\\Users\\Nikitas\\PycharmProjects\\graph_original\\Graph_1", stringizer=None)


    # Parameters
    # ----------
    # n : int
    #     The number of nodes.
    # m : int
    #     The number of edges.
    # seed : integer, random_state, or None (default)
    #     Indicator of random number generation state.
    #     See :ref:`Randomness<randomness>`.
    # directed : bool, optional (default=False)
    #     If True return a directed graph
Graph2 = nx.gnm_random_graph(20, 60, 1, directed=True)
nx.draw(Graph2, edge_labels=True)
plt.show()
nx.write_gml(Graph2, "C:\\Users\\Nikitas\\PycharmProjects\\graph_original\\Graph_2", stringizer=None)



     # n : int
     #     the number of nodes
     # m : int
     #     the number of random edges to add for each new node
     # p : float,
     #     Probability of adding a triangle after adding a random edge
     # seed : integer, random_state, or None (default)
     #     Indicator of random number generation state.
     #     See :ref:`Randomness<randomness>`.

Graph3 = nx.powerlaw_cluster_graph(40, 30, 0.7, seed=None)
nx.draw(Graph3, edge_labels=True)
plt.show()
nx.write_gml(Graph3, "C:\\Users\\Nikitas\\PycharmProjects\\graph_original\\Graph_3", stringizer=None)
