import football as fb
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
# nx.draw(G, edge_labels=True)
# plt.show()
fb.calculate_degree_average_max(Graph1)
clustering_Graph1 = nx.clustering(Graph1)
fb.calculate_average_max(clustering_Graph1, "clustering coefficient" )

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
# nx.draw(G1, edge_labels=True)
# plt.show()
fb.calculate_degree_average_max(Graph2)
clustering_Graph2 = nx.clustering(Graph2)
fb.calculate_average_max(clustering_Graph2, "clustering coefficient" )

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
# nx.draw(G2, edge_labels=True)
# plt.show()
fb.calculate_degree_average_max(Graph3)
clustering_Graph3= nx.clustering(Graph3)
fb.calculate_average_max(clustering_Graph3, "clustering coefficient" )