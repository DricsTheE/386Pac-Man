class Settings():

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200,200,200)

        #self.alien1_points = 10
        #self.alien2_points = 20
        #self.alien3_points = 30

        self.speed_settings()

    def speed_settings(self):
        self.PM_SPD = 2