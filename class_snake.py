import pygame
import datas
from random import randint

class Snake:
    def __init__(self):
        self.size = datas.CELL_SIZE
        self.speed = datas.CELL_SIZE
        self.tail = 100
        self.body = []

    def spawn_snake(self, screen, width, height):
        randx = randint(self.size, width - self.size)
        randy = randint(self.size, height - self.size)
        aligned_x, aligned_y = datas.align_elements(randx, randy, datas.CELL_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), (aligned_x, aligned_y, self.size, self.size), width=1)
        self.body.append([aligned_x, aligned_y])

    def draw_snake(self, screen):
        for i in range(min(self.tail, len(self.body))):
            pygame.draw.rect(screen,(255, 0, 0),(self.body[i][0], self.body[i][1], self.size, self.size),width=2)

    def eat_fruit(self, fruit_loc):
        if fruit_loc == self.body[0]:
            return True
        return False

    def move_right(self, app_width):
        next_localisation = self.body[0][0] + self.speed
        if next_localisation >= app_width or [next_localisation, self.body[0][1]] in self.body:
            return False
        self.body.insert(0, [next_localisation, self.body[0][1]])  # rajoute à l'index 0 la nouvelle position de la tête, permet de faire un mouvement logique du serpent
        return True

    def move_left(self):
        next_localisation = self.body[0][0] - self.speed
        if next_localisation < 0 or [next_localisation, self.body[0][1]] in self.body:
            return False
        self.body.insert(0, [next_localisation, self.body[0][1]])
        return True

    def move_up(self):
        next_localisation = self.body[0][1] - self.speed
        if next_localisation < 0 or [self.body[0][0], next_localisation] in self.body:
            return False
        self.body.insert(0, [self.body[0][0], self.body[0][1] - self.speed])
        return True

    def move_down(self, app_height):
        next_localisation = self.body[0][1] + self.speed
        if next_localisation >= app_height or [self.body[0][0], next_localisation] in self.body:
            return False
        self.body.insert(0, [self.body[0][0], next_localisation])
        return True
