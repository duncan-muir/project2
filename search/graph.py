import networkx as nx
from collections import OrderedDict
from typing import Union, List

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

    def bfs(self, start, end=None) -> Union[None, List[str]]:
        """
        Performs breadth-first search with the follwing behavior:

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None


        """

        # check if starting node is valid, return if none (could be a throw, but returning none makes sense)
        if start not in self.graph:
            return None

        # initialize queue with starting node
        queue = [start]

        # create seen_list / visited set for tracking parents and visitation
        visited = OrderedDict({start: None})

        while len(queue) > 0:
            # queue not empty, pop item (first in list because, appending neighbors at end of list)
            curr = queue.pop(0)

            # check if target reached
            if curr == end:

                # initialize path list
                path = [curr]

                # ascend through path by tracking stored parent relationships, and return final path
                while curr != start:
                    curr = visited[curr]
                    path.insert(0, curr)
                return path

            # find neighbors, add to queue and visited dict if not already existent
            neighbors = self.graph.adj[curr]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = curr

        # graph traversed in entirety, end node not reached, return None
        if end:
            return None

        # no end node provide, return graph traversal
        else:
            return list(visited.keys())




