class Settings():

    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_limit = 3


        #self.bul

        #Ширина пули
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        # Максимальное кол-во пуль на экране
        self.bullets_allowed = 30
        # Настройки пришельцев

        self.fleet_drop_speed = 5
    # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        # Увеличивает настройки скорости и стоимость пришельцев
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
