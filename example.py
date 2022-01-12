from search.graph import Graph
import matplotlib.pyplot as plt
import networkx as nx


def main():
    graph = Graph("data/tiny_network.adjlist")

    print(graph.bfs("Charles Chiu"))

    subax1 = plt.subplot(121)
    nx.draw(graph.graph, with_labels=True, font_weight='bold')
    plt.show()

if __name__ == '__main__':
    main()
