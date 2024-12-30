class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {
            "money": 0,
            "steel": 0,
            "titanium": 0,
            "plants": 0,
            "energy": 0,
            "heat": 0
        }
        self.cards = []
        self.actions = []

    def add_resources(self, resource_type, amount):
        if resource_type in self.resources:
            self.resources[resource_type] += amount

    def remove_resources(self, resource_type, amount):
        if resource_type in self.resources and self.resources[resource_type] >= amount:
            self.resources[resource_type] -= amount

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            # Add code to handle the effects of playing the card

    def add_action(self, action):
        self.actions.append(action)

    def perform_action(self, action):
        if action in self.actions:
            self.actions.remove(action)
            # Add code to handle the effects of performing the action

    def update_player_state(self):
        # Add code to update the player's state
        pass
