from functions import find_max_metrics, find_average_metrics, find_general_metrics
import networkx as nx
import matplotlib.pyplot as plt

football = nx.read_gml('C:\\Users\\Nikitas\\PycharmProjects\\newHelloWorld\\football.gml')

find_general_metrics(football, 'Football Graph')
find_average_metrics(football, 'Football Graph')
find_max_metrics(football, 'Football Graph')

