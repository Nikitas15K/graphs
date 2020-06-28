import networkx as nx
# from functions import create_graph_with_nodes_and_edges


# use function "create_graph_with_nodes_and_edges" to create graph
# create_graph_with_nodes_and_edges(100, 300, "Graph_1")
# create_graph_with_nodes_and_edges(200, 900, "Graph_2")
# create_graph_with_nodes_and_edges(400, 1100, "Graph_3")
# create_graph_with_nodes_and_edges(2000, 7000, "Graph_4")

# use function "create_graph_with_nodes_and_p_for_edges" to create graph
# p is the probability a node connects with another node
# create_graph_with_nodes_and_p_for_edges(100, 0.05,  "Graph_5")
# create_graph_with_nodes_and_p_for_edges(200, 0.05, "Graph_6")
# create_graph_with_nodes_and_p_for_edges(400, 0.02, "Graph_7")
# create_graph_with_nodes_and_p_for_edges(1000, 0.02, "Graph_8")

# initialise empty list to add graphs
graph_list = []

Graph1 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_1.gml')
# delete isolated nodes from graph
Graph1.remove_nodes_from(list(nx.isolates(Graph1)))
graph_list.append(Graph1)

Graph2 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_2.gml')
Graph2.remove_nodes_from(list(nx.isolates(Graph2)))
graph_list.append(Graph2)

Graph3 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_3.gml')
Graph3.remove_nodes_from(list(nx.isolates(Graph3)))
graph_list.append(Graph3)

Graph4 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_4.gml')
Graph4.remove_nodes_from(list(nx.isolates(Graph4)))
graph_list.append(Graph4)

Graph5 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_5.gml')
Graph5.remove_nodes_from(list(nx.isolates(Graph5)))
graph_list.append(Graph5)

Graph6 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_6.gml')
Graph6.remove_nodes_from(list(nx.isolates(Graph6)))
graph_list.append(Graph6)

Graph7 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_7.gml')
Graph7.remove_nodes_from(list(nx.isolates(Graph7)))
graph_list.append(Graph7)

Graph8 = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\Graph_8.gml')
Graph8.remove_nodes_from(list(nx.isolates(Graph8)))
graph_list.append(Graph8)

# create list of graph names
name_list = ["Graph1", "Graph2", "Graph3", "Graph4", "Graph5", "Graph6", "Graph7", "Graph8"]
