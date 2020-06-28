from diffusion_function_nodes_best_metrics import top_5_key_in_values, find_diffusion_from_max_metrics
from graphs import graph_list
import networkx as nx

best_degree_nodes_list = []

for i in range(0, len(graph_list)):
    degree_graph = nx.degree(graph_list[i])
    max_5_degree = top_5_key_in_values(dict(degree_graph))
    best_degree_nodes_list.append(max_5_degree)

for i in range(0, len(graph_list)):
    find_diffusion_from_max_metrics(graph_list[i], best_degree_nodes_list[i], 50)
