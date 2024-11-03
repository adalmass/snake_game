import datas
import pygame
from random import randint

class Fruit:
    def __init__(self, app_win, loc_snake_body):
        self.fruit = None
        self.existing = False
        self.loc = None
        self.spawn_fruit(app_win, loc_snake_body)
        self.draw_fruit(app_win)

    def spawn_fruit(self, screen, loc_snake_body):
        counter = 0
        while True:
            randx = randint(datas.CELL_SIZE, datas.WIN_WIDTH - datas.CELL_SIZE)
            randy = randint(datas.CELL_SIZE, datas.WIN_HEIGHT - datas.CELL_SIZE)
            aligned_x, aligned_y = datas.align_elements(randx, randy, datas.CELL_SIZE)
            self.loc = [aligned_x, aligned_y]
            if self.loc not in loc_snake_body:  # Vérifie s'il n'y a pas un rectangle représentant le corps du serpent à cet emplacement. Si ce n'est aps le cas, alors le fruit spawn ici
                pygame.draw.rect(screen, (255, 0, 0), (aligned_x, aligned_y, datas.CELL_SIZE, datas.CELL_SIZE), width=1)
                return
    def draw_fruit(self, app_win):
        self.fruit = pygame.draw.rect(app_win, (0, 255, 0), (self.loc[0], self.loc[1], datas.CELL_SIZE, datas.CELL_SIZE), width=1)

