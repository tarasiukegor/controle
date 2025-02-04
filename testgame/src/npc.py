# src/npc.py
from dialogue import DialogueSystem

class NPC:
    def __init__(self, name):
        self.name = name
        self.dialogue_system = DialogueSystem()

    def add_dialogue(self, node_id, text, character=None):
        self.dialogue_system.add_dialogue_node(node_id, text, character)

    def add_choice(self, from_node_id, to_node_id, choice_text, condition=None):
        self.dialogue_system.add_choice(from_node_id, to_node_id, choice_text, condition)

    def start_dialogue(self, start_node_id):
        self.dialogue_system.start_dialogue(start_node_id)