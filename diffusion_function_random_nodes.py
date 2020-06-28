import matplotlib.pyplot as plt
import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
import random


def find_diffusion(graph, time_step, k):
    # Model selection
    model = ep.IndependentCascadesModel(graph)
    node_position = nx.spring_layout(graph)

    # Model Configuration
    config = mc.Configuration()
    infected_nodes = random.sample(list(graph.nodes), k)
    config.add_model_initial_configuration("Infected", infected_nodes)
    # note if you wanna use slice for initial infected , use the row below
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

    for i in range(0, time_step):
        print(iterations[i])
        if i > 0:
            y = iterations[i].get('status')
            susceptible = {i: j for i, j in susceptible.items() if i not in y}

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
    print(percentage_of_infected)

    title = "Well, it's been " + str(time_step) + " time steps"
    susceptible_nodes = list(susceptible.keys())
    nx.draw_networkx_nodes(graph, pos=node_position, nodelist=susceptible_nodes, node_size=30, node_color="white",
                           label='Susceptible', edgecolors="black")
    nx.draw_networkx_nodes(graph, pos=node_position, nodelist=infected_nodes, node_size=30, node_color="red",
                           label='Infected', edgecolors="black")
    nx.draw_networkx_nodes(graph, pos=node_position, nodelist=removed_nodes, node_size=30, node_color="yellow",
                           label='Removed', edgecolors="black")
    nx.draw_networkx_edges(graph, pos=node_position)
    nx.draw_networkx_labels(graph, pos=node_position, font_size=10)
    plt.legend(scatterpoints=1)
    plt.title(label=title)
    plt.show()
