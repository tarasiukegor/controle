class DialogueManager:
    def __init__(self):
        self.dialogues = {
            "Tavern NPC": {
                "text": "Greetings, traveler! Do you seek a quest?",
                "options": {
                    "Yes": "Find the lost sword in the Forest.",
                    "No": "Come back when you're ready."
                }
            }
        }

    def get_dialogue(self, npc):
        return self.dialogues.get(npc, {"text": "I have nothing to say.", "options": {}})
