class GameStats:
    def __init__(self, aiGame):
        self.set = aiGame.set
        self.record = aiGame.getRecord()
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.set.ship_limit
        self.score = 0
        self.level = 1