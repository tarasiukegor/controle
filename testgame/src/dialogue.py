# src/dialogue.py
from graph import Graph, GraphNode

class DialogueSystem:
    def __init__(self):
        self.graph = Graph()
        self.current_node = None

    def add_dialogue_node(self, node_id, text, character=None):
        node = GraphNode(node_id, {"text": text, "character": character})
        self.graph.add_node(node)

    def add_choice(self, from_node_id, to_node_id, choice_text, condition=None):
        from_node = self.graph.get_node(from_node_id)
        to_node = self.graph.get_node(to_node_id)
        if from_node and to_node:
            from_node.add_edge(to_node, condition)

    def start_dialogue(self, start_node_id):
        self.current_node = self.graph.get_node(start_node_id)

    def get_current_dialogue(self):
        if self.current_node:
            return self.current_node.data
        return None

    def make_choice(self, choice_index):
        if self.current_node and choice_index < len(self.current_node.edges):
            self.current_node = self.current_node.edges[choice_index]["target"]
            return True
        return False