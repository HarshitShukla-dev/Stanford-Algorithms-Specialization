import random
import copy

class KargerMinCutter:
    def __init__(self, graph_file):
        self._graph = {}
        self._total_edges = 0
        with open(graph_file) as file:
            for index, line in enumerate(file):
                numbers = [int(number) for number in line.split()]
                self._graph[numbers[0]] = numbers[1:]
                self._total_edges += len(numbers) - 1

    def find_min_cut(self):
        while len(self._graph) > 2:
            v1, v2 = self._pick_random_edge()
            self._total_edges -= len(self._graph[v1])
            self._total_edges -= len(self._graph[v2])
            self._graph[v1].extend(self._graph[v2])
            for vertex in self._graph[v2]:
                self._graph[vertex].remove(v2)
                self._graph[vertex].append(v1)
            self._graph[v1] = [v for v in self._graph[v1] if v != v1]
            self._total_edges += len(self._graph[v1])
            self._graph.pop(v2)
        return len(list(self._graph.values())[0])

    def _pick_random_edge(self):
        rand_edge = random.randint(0, self._total_edges - 1)
        for vertex, vertex_edges in self._graph.items():
            if len(vertex_edges) <= rand_edge:
                rand_edge -= len(vertex_edges)
            else:
                from_vertex = vertex
                to_vertex = vertex_edges[rand_edge]
                return from_vertex, to_vertex

if __name__ == "__main__":
    min_cut = 99999
    min_cutter = KargerMinCutter('intArray.txt')
    num_iterations = 40000
    for i in range(num_iterations):
        graph_copy = copy.deepcopy(min_cutter._graph)
        min_cutter._graph = graph_copy
        cut = min_cutter.find_min_cut()
        if cut < min_cut:
            min_cut = cut
    print(min_cut)
