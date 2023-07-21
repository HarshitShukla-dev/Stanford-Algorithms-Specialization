from collections import defaultdict

class SccFinder:
    def __init__(self, input_file):
        """
        Initializes the Strongly Connected Components (SCC) Finder.

        Args:
            input_file (str): Path to the input file containing directed edges.
        """
        self.scc_list = []
        with open(input_file) as file:
            self.finish_order = []
            self._graph = defaultdict(list)
            for line in file:
                from_v, to_v = tuple(map(int, line.split()))
                self._add_edge_to_graph(from_v, to_v)

    def _add_edge_to_graph(self, from_v, to_v):
        """
        Adds a directed edge to the graph.

        Args:
            from_v (int): Source vertex of the edge.
            to_v (int): Target vertex of the edge.
        """
        self._graph[from_v].append(to_v)
        self._graph[to_v].append(-from_v)

    def compute_finish_times(self):
        """
        Computes the finish times of the vertices using depth-first search (DFS).
        """
        visited_nodes, finished_nodes = set(), set()
        for vertex in self._graph.keys():
            if vertex in visited_nodes:
                continue
            nodes_stack = [vertex]
            while nodes_stack:
                node = nodes_stack.pop()
                if node not in visited_nodes:
                    visited_nodes.add(node)
                    nodes_stack.append(node)
                    neighbors = (-edge for edge in self._graph[node] if edge < 0)
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            nodes_stack.append(neighbor)
                else:
                    if node not in finished_nodes:
                        self.finish_order.append(node)
                        finished_nodes.add(node)

    def compute_sccs(self):
        """
        Computes the sizes of the Strongly Connected Components (SCCs) using finish times.
        """
        visited_nodes = set()
        assert (len(self.finish_order) == len(self._graph))
        for i in reversed(self.finish_order):
            if i in visited_nodes:
                continue
            nodes_stack = [i]
            size = 0
            while nodes_stack:
                node = nodes_stack.pop()
                if node not in visited_nodes:
                    size += 1
                    visited_nodes.add(node)
                    nodes_stack.append(node)
                    neighbors = (edge for edge in self._graph[node] if edge > 0)
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            nodes_stack.append(neighbor)
            self.scc_list.append(size)
        self.scc_list.sort(reverse=True)
        print(self.scc_list[:5])

if __name__ == "__main__":
    scc_finder = SccFinder("intArray.txt")
    scc_finder.compute_finish_times()
    scc_finder.compute_sccs()
    expected_sccs = [434821, 968, 459, 313, 211]
    print(scc_finder.scc_list[:5])

# Output: [434821, 968, 459, 313, 211]