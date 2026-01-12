class Settings:
    """Класс для хранения настроек игры Space War"""

    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bg = (142, 184, 229)
        self.shipSpeed = 1.5
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (242, 221, 110)
        self.bullets_allowed = 5