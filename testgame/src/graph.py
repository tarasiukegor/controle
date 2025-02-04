# src/graph.py
class GraphNode:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data  # Can store dialogue text, quest details, etc.
        self.edges = []  # List of edges (connections to other nodes)

    def add_edge(self, target_node, condition=None):
        self.edges.append({
            "target": target_node,
            "condition": condition  # Optional condition for traversal
        })

class Graph:
    def __init__(self):
        self.nodes = {}  # Store nodes by ID

    def add_node(self, node):
        self.nodes[node.id] = node

    def get_node(self, node_id):
        return self.nodes.get(node_id)