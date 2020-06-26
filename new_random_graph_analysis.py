from football import calculate_average_max, calculate_degree_average_max as fb
import networkx as nx

fb.calculate_degree_average_max(Graph1)
clustering_Graph1 = nx.clustering(Graph1)
fb.calculate_average_max(clustering_Graph1, "clustering coefficient" )

fb.calculate_degree_average_max(Graph2)
clustering_Graph2 = nx.clustering(Graph2)
fb.calculate_average_max(clustering_Graph2, "clustering coefficient" )

fb.calculate_degree_average_max(Graph3)
clustering_Graph3= nx.clustering(Graph3)
fb.calculate_average_max(clustering_Graph3, "clustering coefficient" )