class Graph:
    def __init__(self, v_count):
        self.graph = [[] for _ in range(v_count)]

    def v_count(self):
        return len(self.graph)

    def add_weighted_edge(self, v1, v2, weight):
        self.graph[v1].append((v2, weight))
        self.graph[v2].append((v1, weight))

    def dfs_weight_count(self, v0, used, weights, component_number, prev = None):
        if v0 in used:
            return
        used.add(v0)
        for v in self.graph[v0]:
            if v[0] != prev:
                weights[component_number] += v[1]
                self.dfs_weight_count(v[0], used, weights, component_number, v0)

    def components_weight_count(self):
        used = set()
        weights = []
        component_number = 0
        for v in range(self.v_count()):
            if not(v in used):
                weights.append(0)
                self.dfs_weight_count(v, used, weights, component_number)
                component_number += 1
        return weights


if __name__ == '__main__':
    v_count, edges_count = map(int, input().split())
    graph = Graph(v_count)
    for _ in range(edges_count):
        v1, v2, weight = map(int, input().split())
        graph.add_weighted_edge(v1, v2, weight)
    answer = graph.components_weight_count()
    print('\n'.join(map(str, answer)))



