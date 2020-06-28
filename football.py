from functions import calculate_general_metrics, calculate_average_metrics, calculate_max_metrics
import networkx as nx

football = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\football.gml')

calculate_general_metrics(football, 'Football Graph')
calculate_max_metrics(football, 'Football Graph')
calculate_average_metrics(football, 'Football Graph')
