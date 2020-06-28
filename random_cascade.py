from diffusion_function_random_nodes import find_diffusion
from graphs import graph_list

# get cascade diffusion for every graph in graph list, 40 iterations and random sample of 5 nodes for initial infection
for i in range(0, len(graph_list)):
    find_diffusion(graph_list[i], 40, 5)
