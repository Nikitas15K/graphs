from functions import calculates_max_metrics, calculates_general_metrics, calculates_average_metrics
from graphs import graph_list, name_list

for i in range(0, len(graph_list)):
    calculates_general_metrics(graph_list[i], name_list[i])
    calculates_max_metrics(graph_list[i], name_list[i])
    calculates_average_metrics(graph_list[i], name_list[i])
