from football import calculate_average_max, calculate_degree_average_max as fb
import networkx as nx

Graph1= nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\graph_original\\Graph_1.gml')
Graph2= nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\graph_original\\Graph_2.gml')
Graph3= nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\graph_original\\Graph_3.gml')

fb.calculate_degree_average_max(Graph1)
clustering_Graph1 = nx.clustering(Graph1)
fb.calculate_average_max(clustering_Graph1, "clustering coefficient" )

fb.calculate_degree_average_max(Graph2)
clustering_Graph2 = nx.clustering(Graph2)
fb.calculate_average_max(clustering_Graph2, "clustering coefficient" )

fb.calculate_degree_average_max(Graph3)
clustering_Graph3= nx.clustering(Graph3)
fb.calculate_average_max(clustering_Graph3, "clustering coefficient" )