# write tests for bfs
import pytest
from search import Graph


def test_bfs_traversal_micro():
    """
    Test that traversal occurs properly on micro_network
    """
    graph = Graph("./data/micro_network.adjlist")
    traversal = graph.bfs("Lani Wu")
    assert traversal == ["Lani Wu", "32042149", "32036252",
                         "31806696", "Hani Goodarzi", "Luke Gilbert"]


def test_bfs_traversal_tiny():
    """
    Test that traversal occurs properly on tiny_network
    """
    graph = Graph("./data/tiny_network.adjlist")
    traversal = graph.bfs("Charles Chiu")
    assert traversal == ["Charles Chiu", "33242416", "Atul Butte",
                         "33765435", "31395880", "30944313",
                         "Marina Sirota", "Steven Altschuler", "Lani Wu",
                         "Hani Goodarzi", "Nevan Krogan", "31486345",
                         "32036252", "32042149", "31806696",
                         "30727954", "33232663", "34272374",
                         "32353859", "Michael Keiser",
                         "Luke Gilbert", "Michael McManus", "Martin Kampmann",
                         "33483487", "31626775", "31540829",
                         "32025019", "29700475", "32790644", "Neil Risch"]


def test_bfs_tiny():
    """
    Test finding shortest (4 edge) path in citation network
    """
    graph = Graph("./data/tiny_network.adjlist")

    path = graph.bfs("Nevan Krogan", "Luke Gilbert")

    assert len(path) == 5
    assert path == ["Nevan Krogan", "34272374", "Martin Kampmann",
                    "33483487", "Luke Gilbert"]


def test_bfs_citation():
    """
    Test finding shortest (2 edge) path in citation network
    """
    graph = Graph("./data/citation_network.adjlist")

    path = graph.bfs("Nevan Krogan", "Luke Gilbert")

    assert len(path) == 3
    assert path == ["Nevan Krogan", "33904395", "Luke Gilbert"]


def test_bfs_fail_micro():
    """
    Test failure on micro_network where no valid path exists
    """
    graph = Graph("./data/micro_network.adjlist")
    path = graph.bfs("Lani Wu", "Neil Risch")
    assert path is None


def test_bfs_fail_tiny():
    """
    Test failure on tiny_network when end node is not in graph
    """
    graph = Graph("./data/tiny_network.adjlist")
    path = graph.bfs("Lani Wu", "Bob Barker")
    assert path is None


def test_bfs_traversal_fail_citation():
    """
    Test traversal failure when start does not exist
    """
    graph = Graph("./data/citation_network.adjlist")

    path = graph.bfs("James Bond")

    assert path is None


def test_bfs_fail_citation():
    """
    Test search failure when start does not exist
    """
    graph = Graph("./data/citation_network.adjlist")

    path = graph.bfs("James Bond", "Luke Gilbert")

    assert path is None
