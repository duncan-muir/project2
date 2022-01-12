import networkx as nx
from collections import OrderedDict

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        # initialize queue with starting node
        queue = [start]

        visited = OrderedDict({start: None})

        while len(queue) > 0:
            curr = queue.pop(0)

            if curr == end:
                path = [curr]
                while curr != start:
                    curr = visited[curr]
                    path.insert(0, curr)
                return path

            neighbors = self.graph.adj[curr]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = curr

        if end:
            return None
        else:
            return list(visited.keys())




