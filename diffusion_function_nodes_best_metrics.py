import matplotlib.pyplot as plt
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep


def top_5_key_in_values(data):
    sorted_data = sorted(data, key=data.get, reverse=True)
    top_5_data = sorted_data[0:5]
    top_nodes = []
    for r in top_5_data:
        top_nodes.append(r)
    return top_nodes


def find_diffusion_from_max_metrics(graph, node_list, time_step):
    # Model selection
    model = ep.IndependentCascadesModel(graph)
    node_position = nx.spring_layout(graph)

    # Model Configuration
    config = mc.Configuration()

    # diffusion for every best set of nodes
    name_list = ["clustering coefficient", "betweeness", "eigenvector centrality", "degree"]

    config.add_model_initial_configuration('Infected', node_list)
    # config.add_model_parameter('fraction_infected',0.1)

    # Setting the edge parameters
    threshold = 0.25
    for e in graph.edges():
        config.add_edge_configuration("threshold", e, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(time_step)

    susceptible = iterations[0].get('status')
    altered_nodes = dict()

    for ii in range(0, time_step):
        print(iterations[ii])
        if ii > 0:
            y = iterations[ii].get('status')
            susceptible = {ii: jj for ii, jj in susceptible.items() if ii not in y}

            result = dict(y.items() - susceptible.items())
            altered_nodes.update(result)

    infected_status = 1
    infected_nodes = []
    removed_nodes = []
    for node, status in altered_nodes.items():
        if status == infected_status:
            infected_nodes.append(node)
        else:
            removed_nodes.append(node)

    percentage_of_infected = (len(infected_nodes) + len(removed_nodes)) / int(nx.number_of_nodes(graph))

    # print(len(infected_nodes))
    # print(len(removed_nodes))
    # print(int(nx.number_of_nodes(graph)))
    print(percentage_of_infected)

    title = "The node status after " + str(time_step) + " time steps"
    susceptible_nodes = list(susceptible.keys())
    nx.draw_networkx_nodes(graph, pos=node_position, nodelist=susceptible_nodes, node_size=20, node_color="white",
                               label='Susceptible', edgecolors="black")
    nx.draw_networkx_nodes(graph, pos=node_position, nodelist=infected_nodes, node_size=20, node_color="red",
                               label='Infected', edgecolors="black")
    nx.draw_networkx_nodes(graph, pos=node_position, nodelist=removed_nodes, node_size=20, node_color="blue",
                               label='Removed', edgecolors="black")
    nx.draw_networkx_edges(graph, pos=node_position)
    nx.draw_networkx_labels(graph, pos=node_position, font_size=10)
    plt.legend(scatterpoints=1)
    plt.title(label=title)
    plt.show()

