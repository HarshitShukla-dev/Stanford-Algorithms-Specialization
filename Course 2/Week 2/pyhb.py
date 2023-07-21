from ast import literal_eval


class DijkstraPathFinder:
    """
    DijkstraPathFinder class finds the shortest paths in a graph using Dijkstra's algorithm.

    Args:
        input_file (str): The name of the input file containing the graph information.

    Attributes:
        graph (dict): A dictionary representing the graph with vertices as keys and their adjacent edges as values.
        source_vertex (int): The source vertex used for computing shortest paths.

    """

    def __init__(self, input_file):
        self.graph = {}
        with open(input_file) as file:
            for line in file:
                vertex, *edges = map(literal_eval, line.split())
                self.graph[vertex] = edges
        self.source_vertex = next(iter(self.graph.keys()))

    def compute_shortest_paths(self, source=None):
        """
        Compute the shortest paths from the given source vertex to all other vertices in the graph.

        Args:
            source (int, optional): The source vertex for computing shortest paths. If not provided,
            the default source vertex set during object initialization will be used.

        Returns:
            dict: A dictionary containing vertex as keys and the corresponding shortest distance and path as values.

        """
        if source is None:
            source = self.source_vertex

        # Initialize shortest_paths dictionary with initial distances as infinite and empty paths.
        shortest_paths = {vertex: (float('inf'), []) for vertex in self.graph.keys()}
        shortest_paths[source] = (0, [])

        visited = set()
        while set(self.graph.keys()) - visited:
            source_vertex, min_edge = None, ()
            for vertex in visited:
                for edge_vertex, edge_distance in self.graph[vertex]:
                    if edge_vertex in visited:
                        continue
                    new_distance = shortest_paths[vertex][0] + edge_distance
                    if not min_edge or new_distance < min_edge[1]:
                        min_edge = (edge_vertex, new_distance)
                        source_vertex = vertex
            if source_vertex is None:
                break  # All reachable vertices have been visited
            shortest_paths[min_edge[0]] = (min_edge[1], shortest_paths[source_vertex][1] + [min_edge[0]])
            visited.add(min_edge[0])

        return shortest_paths


if __name__ == '__main__':
    path_finder = DijkstraPathFinder('intArray.txt')
    shortest_distances = path_finder.compute_shortest_paths()
    vertices_to_print = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

    # Print the shortest distances for the specified vertices separated by commas
    output = ','.join(str(shortest_distances[vertex][0]) for vertex in vertices_to_print)
    print(output)
