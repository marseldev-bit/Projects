class Settings:
    """Класс для хранения настроек игры Space War"""

    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bg = (142, 184, 229)
        self.shipSpeed = 2.5
        self.ship_limit = 3
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (242, 221, 110)
        self.bullets_allowed = 5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1