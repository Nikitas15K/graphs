from diffusion_function_nodes_best_metrics import top_5_key_in_values, find_diffusion_from_max_metrics
from graphs import graph_list
import networkx as nx

best_betweeness_nodes_list = []

for i in range(0, len(graph_list)):
    betweeness_graph = nx.betweenness_centrality(graph_list[i])
    max_5_betweeness = top_5_key_in_values(betweeness_graph)
    best_betweeness_nodes_list.append(max_5_betweeness)

for i in range(0, len(graph_list)):
    find_diffusion_from_max_metrics(graph_list[i], best_betweeness_nodes_list[i], 50)
