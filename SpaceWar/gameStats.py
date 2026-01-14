class GameStats:
    def __init__(self, aiGame):
        self.set = aiGame.set
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.set.ship_limit