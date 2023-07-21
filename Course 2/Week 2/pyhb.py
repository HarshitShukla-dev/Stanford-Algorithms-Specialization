from ast import literal_eval

class DijkstraPathFinder:
    """
    DijkstraPathFinder class computes the shortest paths in a graph using Dijkstra's algorithm.

    Attributes:
        graph (dict): A dictionary representing the graph with vertex as keys and lists of edges as values.
        source_vertex (int): The source vertex for computing the shortest paths.
    """

    def __init__(self, input_file):
        """
        Initialize the DijkstraPathFinder with a graph from the input file.

        Args:
            input_file (str): The path to the input file containing the graph information.
        """
        self.graph = {}
        with open(input_file) as file:
            for line in file:
                vertex, *edges = map(literal_eval, line.split())
                self.graph[vertex] = edges
        self.source_vertex = next(iter(self.graph.keys()))

    def compute_shortest_paths(self, source=None):
        """
        Compute the shortest paths from the source vertex to all other vertices using Dijkstra's algorithm.

        Args:
            source (int, optional): The source vertex. If not provided, the default source vertex will be used.

        Returns:
            dict: A dictionary containing the shortest distances from the source vertex to all other vertices.
        """
        if source is None:
            source = self.source_vertex

        INF = float('inf')
        shortest_distances = {vertex: INF for vertex in self.graph.keys()}
        shortest_distances[source] = 0

        visited = set()

        while len(visited) < len(self.graph):
            min_distance_vertex = min((v for v in self.graph.keys() if v not in visited), key=shortest_distances.get)
            visited.add(min_distance_vertex)

            for neighbor, edge_weight in self.graph[min_distance_vertex]:
                if neighbor not in visited:
                    new_distance = shortest_distances[min_distance_vertex] + edge_weight
                    if new_distance < shortest_distances[neighbor]:
                        shortest_distances[neighbor] = new_distance

        return shortest_distances


if __name__ == '__main__':
    path_finder = DijkstraPathFinder('intArray.txt')
    shortest_distances = path_finder.compute_shortest_paths()

    # Print the shortest distances for the specified vertices
    vertices_of_interest = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    output = [shortest_distances[vertex] for vertex in vertices_of_interest]
    print(','.join(map(str, output)))
