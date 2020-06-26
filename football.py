import networkx as nx
import matplotlib.pyplot as plt
import statistics

football= nx.read_gml('C:\\Users\\Nikitas\\Desktop\\ME1904_ME1905\\xalki2\\football.gml')
nx.draw(football, edge_labels=True)
plt.show()
#
# graph_edges=int(nx.number_of_edges(football))
# print("Graph football edges:" + str(graph_edges))
# graph_nodes=nx.number_of_nodes(football)
# print("Graph football nodes:" + str(graph_nodes))
# graph_average_shortest_path_length=nx.average_shortest_path_length(football)
# print("Graph average shortest path:" + str(graph_average_shortest_path_length))

betweenness_football = nx.betweenness_centrality(football)
# print('Graph football betweeness centrality:' +str(betweenness_football))

clustering_football = nx.clustering(football)
# print('Graph football clustering: ' + str(clustering_football))

eigenvector_centrality_football = nx.eigenvector_centrality(football)
# print('Graph football eigenvector centrality: ' + str(eigenvector_centrality_football))

closeness_centrality_football= nx.closeness_centrality(football)
# print('Graph closeness centrality football: ' + str(closeness_centrality_football))


# print('Graph football degree: ' + str(degree_football))

def calculate_average_max(data, measure):
    # a1_sorted_keys = sorted(data, key=data.get, reverse=True)
    # for r in a1_sorted_keys:
    #     print(r, data[r])
    # print("\n")
    average = 0
    sum = 0
    for key in data.keys():
        sum = sum + data[key]
    average = sum / len(data)
    max_key = max(data , key=data.get)
    maxvalue=max(data.values())
    print('Average ' + str(measure) + " is: " +str(average))
    print('Max '+ str(measure) + ' is: ' + str(max_key) + ' : ' + str(maxvalue))
    print("\n")

calculate_average_max(betweenness_football, "betweeness")
calculate_average_max(clustering_football, "clustering coefficient" )
calculate_average_max(eigenvector_centrality_football, "eigenvector centrality")
calculate_average_max(closeness_centrality_football, "closeness centrality")

def calculate_degree_average_max(data):
    degree = nx.degree(data)
    maxvalue = 0
    counter = 0
    sumRank = 0
    max_key=[]
    for i in degree:
        sumRank+=i[1]
        counter = counter+1
        if maxvalue <= i[1]:
            maxvalue=i[1]
            max_key.append(i[0])
    degree_average = sumRank/counter
    print("Average degree: " + str(degree_average))
    print('Max degree is: ' + str(max_key) + ' : ' + str(maxvalue))
    print("\n")

calculate_degree_average_max(football)