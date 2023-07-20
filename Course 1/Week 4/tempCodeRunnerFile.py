import random
import copy

class KargerMinCutter:
    def __init__(self, graph_file):
        self._graph = {}
        with open(graph_file) as file:
            for line in file:
                numbers = [int(number) for number in line.split()]
                self._graph[numbers[0]] = numbers[1:]

    def find_min_cut(self):
        while len(self._graph) > 2:
            v1, v2 = self._pick_random_edge()
            self._contract_vertices(v1, v2)
        return len(list(self._graph.values())[0])

    def _pick_random_edge(self):
        v1 = random.choice(list(self._graph.keys()))
        v2 = random.choice(self._graph[v1])
        return v1, v2

    def _contract_vertices(self, v1, v2):
        self._graph[v1].extend(self._graph[v2])
        for vertex in self._graph[v2]:
            self._graph[vertex].remove(v2)
            self._graph[vertex].append(v1)
        self._graph[v1] = [v for v in self._graph[v1] if v != v1]
        self._graph.pop(v2)

if __name__ == "__main__":
    min_cut = float('inf')
    min_cutter = KargerMinCutter('intArray.txt')
    num_iterations = 40000
    for i in range(num_iterations):
        graph_copy = copy.deepcopy(min_cutter._graph)
        min_cutter._graph = graph_copy
        cut = min_cutter.find_min_cut()
        if cut < min_cut:
            min_cut = cut
    print(min_cut)
import random
import copy

class KargerMinCutter:
    def __init__(self, graph_file):
        self._graph = {}
        with open(graph_file) as file:
            for line in file:
                numbers = [int(number) for number in line.split()]
                self._graph[numbers[0]] = numbers[1:]

    def find_min_cut(self):
        while len(self._graph) > 2:
            v1, v2 = self._pick_random_edge()
            self._contract_vertices(v1, v2)
        return len(list(self._graph.values())[0])

    def _pick_random_edge(self):
        v1 = random.choice(list(self._graph.keys()))
        v2 = random.choice(self._graph[v1])
        return v1, v2

    def _contract_vertices(self, v1, v2):
        self._graph[v1].extend(self._graph[v2])
        for vertex in self._graph[v2]:
            self._graph[vertex].remove(v2)
            self._graph[vertex].append(v1)
        self._graph[v1] = [v for v in self._graph[v1] if v != v1]
        self._graph.pop(v2)

if __name__ == "__main__":
    min_cut = float('inf')
    min_cutter = KargerMinCutter('intArray.txt')
    num_vertices = len(min_cutter._graph)
    num_iterations = num_vertices ** 2
    for i in range(num_iterations):
        graph_copy = copy.deepcopy(min_cutter._graph)
        min_cutter._graph = graph_copy
        cut = min_cutter.find_min_cut()
        if cut < min_cut:
            min_cut = cut
    print(min_cut)
