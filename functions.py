import matplotlib.pyplot as plt
import networkx as nx


# method that creates and saves graphs
def create_graph_with_nodes_and_edges(nodes, edges, graph_name):
    graph = nx.gnm_random_graph(nodes, edges, 1, directed=False)
    nx.draw(graph, edge_labels=True)
    plt.show()
    nx.write_gml(graph, "C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\" + graph_name + ".gml", stringizer=None)


# nodes(int) – The number of nodes.
# p(float) – Probability for edge creation
def create_graph_with_nodes_and_p_for_edges(nodes, p, graph_name):
    graph = nx.erdos_renyi_graph(nodes, p)
    nx.draw(graph, edge_labels=True)
    plt.show()
    nx.write_gml(graph, "C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\" + graph_name + ".gml", stringizer=None)


# method that calculates general graph information and plot it
def calculates_general_metrics(graph, graph_name):
    print(graph_name)
    graph_nodes = nx.number_of_nodes(graph)
    print(graph_name + " nodes:" + str(graph_nodes))
    graph_edges = int(nx.number_of_edges(graph))
    print(graph_name + " edges:" + str(graph_edges))
    # nx.draw(graph, edge_labels=True)
    # plt.show()


# method that calculates average value
def calculate_average(data, measure):
    value_sum = 0
    for key, value in data.items():
        value_sum = value_sum + data[key]
    average = value_sum / len(data)
    print(measure + ' Average  is: ' + str(average))
    return average


# method that calculates max value
def calculate_max(data, measure):
    max_keys = []
    max_value = 0
    for key, value in data.items():
        max_value = max(data.values())
        if data[key] == max_value:
            max_keys.append(key)
    print(measure + ' Max is: ', max_keys, ' : ', max_value)
    return max_keys, max_value


# method that calculates max degree for a graph
def calculate_degree_max(graph):
    degree = nx.degree(graph)
    # print('Graph football degree: ' + str(degree_football))
    degree_max_value = 0
    max_key = []
    for i in degree:
        if degree_max_value <= i[1]:
            degree_max_value = i[1]
            max_key.append(i[0])
    print('Degree Max is: ', max_key, ' : ', degree_max_value)
    return max_key, degree_max_value


# method that calculates average degree for a graph
def calculate_degree_average(graph):
    degree = nx.degree(graph)
    counter = 0
    sum_degree = 0
    for i in degree:
        sum_degree += i[1]
        counter = counter + 1
    degree_average = sum_degree / counter
    print("Degree Average is: ", degree_average)


# calculates average metrics
def calculates_average_metrics(graph, graph_name):
    print(graph_name + " average")
    clustering_graph = nx.clustering(graph)
    calculate_average(clustering_graph, "clustering coefficient")
    betweenness_graph = nx.betweenness_centrality(graph)
    calculate_average(betweenness_graph, "Betweeness")
    eigenvector_centrality_graph = nx.eigenvector_centrality(graph)
    calculate_average(eigenvector_centrality_graph, "Eigenvector centrality")
    closeness_centrality_graph = nx.closeness_centrality(graph)
    calculate_average(closeness_centrality_graph, "Closeness centrality")
    calculate_degree_average(graph)
    print("\n")


# calculates max metrics
def calculates_max_metrics(graph, graph_name):
    metrics_list = []
    print(graph_name + " max")
    clustering_graph = nx.clustering(graph)
    max_clustering = calculate_max(clustering_graph, "Clustering coefficient")
    metrics_list.append(max_clustering)
    betweeness_graph = nx.betweenness_centrality(graph)
    max_betweeness = calculate_max(betweeness_graph, "Betweeness")
    metrics_list.append(max_betweeness)
    eigenvector_centrality_graph = nx.eigenvector_centrality(graph)
    max_eigenvector_centrality = calculate_max(eigenvector_centrality_graph, "Eigenvector centrality")
    metrics_list.append(max_eigenvector_centrality)
    closeness_centrality_graph = nx.closeness_centrality(graph)
    max_closeness_centrality = calculate_max(closeness_centrality_graph, "Closeness centrality")
    metrics_list.append(max_closeness_centrality)
    max_degree = calculate_degree_max(graph)
    metrics_list.append(max_degree)
    return list
