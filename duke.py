class Graph:
    def __init__(self, v_count):
        self.graph = [[] for _ in range(v_count)]

    def v_count(self):
        return len(self.graph)

    def add_weighted_edge(self, v1, v2, weight):
        self.graph(v1).append((v2, weight))
        self.graph(v2).append((v1, weight))

    def dfs_weight_count(self, v0, element_weight, used):
        if v0 in used:
            return
        for v in self.graph(v0):
            self.dfs_weight_count(v[0], element_weight + v[1], used)

    def components_weight_count(self):
        used = set()
        weights = []
        component_number = 0
        for v in range(self.v_count()):
            if not(v in used):
                weights[0].append([])


