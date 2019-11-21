class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # 飞船的设置
        self.ship_speed_factor = 50
        self.ship_limit = 2

        # fleet_direction 为1表示向右，为－1表示向左
        self.fleet_direction = 1

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30

        # 外星人设置
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 50
        self.alien_points = 50
        # 外星人点数的提高速度
        self.score_scale = 1.5

        # 以什么的速度加快游戏节奏
        self.speedup_scale = 3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 30
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 5

        # fleet_direction 为1表示向右，为－1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
