import random
import copy

class KargerMinCutter:
    def __init__(self):
        self._graph = {}
        self._total_edges = 0

    def read_graph(self, graph_file):
        with open(graph_file) as file:
            for line in file:
                numbers = [int(number) for number in line.split()]
                self._graph[numbers[0]] = numbers[1:]
                self._total_edges += len(numbers[1:])

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
        v1 = random.choice(list(self._graph.keys()))
        v2 = random.choice(self._graph[v1])
        return v1, v2

if __name__ == "__main__":
    min_cut = 99999
    min_cutter = KargerMinCutter()
    min_cutter.read_graph('intArray.txt')
    num_iterations = 40000
    for i in range(num_iterations):
        graph_copy = copy.deepcopy(min_cutter._graph)
        cut = min_cutter.find_min_cut()
        if cut < min_cut:
            min_cut = cut
    print(min_cut)
#Output:17