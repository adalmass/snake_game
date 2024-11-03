import pygame
import class_snake
import class_fruit
import datas
import json

class App:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = None
        self.width = datas.WIN_WIDTH
        self.height = datas.WIN_HEIGHT
        self.score = 1
        self.record = 1
        #
        self.init_pygame()
        self.running = True
        self.load_record()
        ###
        self.snake = class_snake.Snake()
        self.snake.spawn_snake(self.win, self.width, self.height)
        self.fruit = class_fruit.Fruit(self.win, self.snake.body)
        self.run_game()

    def init_pygame(self):
        pygame.init()
        pygame.font.init()
        self.win = pygame.display.set_mode((self.width, self.height))
        self.font =  pygame.font.Font(None, 25)
        self.refresh_texts()

    def refresh_texts(self):
        self.score_txt = self.font.render(f"Taille: {self.score}", True, datas.TEXT_COLOR)
        self.record_txt = self.font.render(f"Record: {self.record}", True, datas.TEXT_COLOR)

    def save_record(self):
        if self.score > self.record:
            with open("record.json", "w") as f:
                json.dump({"record": self.score}, f)

    def load_record(self):
        try:
            with open("record.json", "r") as f:
                data = json.load(f)
                self.record = data["record"]
                return
        except FileNotFoundError:
            print("file does not found")

    def travelling(self, event):
        if event.key == pygame.K_ESCAPE:
            self.running = False
        # __gauche
        if event.key == pygame.K_a or event.key == pygame.K_q or event.key == pygame.K_LEFT:
            self.running = self.snake.move_left()
        # __droite
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.running = self.snake.move_right(self.width)
        # __haut
        elif event.key == pygame.K_w or event.key == pygame.K_z or event.key == pygame.K_UP:
            self.running = self.snake.move_up()
        # __bas
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.running = self.snake.move_down(self.height)
        if not self.snake.eat_fruit(self.fruit.loc):
            self.snake.body.pop() # supprime le dernier élément de la liste car on rajoute un élément pour que le mouvement soit fluide, du coup on enlève le dernier élément
        else:
            self.snake.tail += 1
            self.score += 1
            self.fruit = None
            self.fruit = class_fruit.Fruit(self.win, self.snake.body)

    def run_game(self):
        while self.running:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.travelling(event)
            self.win.fill((0, 0, 0))  # réinitialiser l'affichage de la fenêtre
            self.win.blit(self.score_txt, (20, 20))
            self.win.blit(self.record_txt, (20, 40))
            self.snake.draw_snake(self.win)
            self.fruit.draw_fruit(self.win)
            self.refresh_texts()
            pygame.display.flip()
            self.clock.tick(datas.FPS)
        self.save_record()