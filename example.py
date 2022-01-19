from search.graph import Graph


def main():
    graph = Graph("data/tiny_network.adjlist")

    print(graph.bfs("Rosalind Franklin"))


if __name__ == '__main__':
    main()
