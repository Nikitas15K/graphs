from diffusion_function_nodes_best_metrics import top_5_key_in_values, find_diffusion_from_max_metrics
from graphs import graph_list
import networkx as nx

best_eigenvector_centrality_nodes_list = []

for i in range(0, len(graph_list)):
    eigenvector_centrality_graph = nx.eigenvector_centrality(graph_list[i])
    max_5_eigenvector_centrality = top_5_key_in_values(eigenvector_centrality_graph)
    best_eigenvector_centrality_nodes_list.append(max_5_eigenvector_centrality)

for i in range(0, len(graph_list)):
    find_diffusion_from_max_metrics(graph_list[i], best_eigenvector_centrality_nodes_list[i], 50)
