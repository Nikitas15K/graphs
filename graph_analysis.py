from functions import calculate_max_metrics, calculate_general_metrics, calculate_average_metrics
from graphs import graph_list, name_list

for i in range(0, len(graph_list)):
    calculate_general_metrics(graph_list[i], name_list[i])
    calculate_max_metrics(graph_list[i], name_list[i])
    calculate_average_metrics(graph_list[i], name_list[i])
