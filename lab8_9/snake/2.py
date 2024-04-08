import pygame
import sys
from pygame.math import Vector2
import random

class WALL:
    def __init__(self):
        self.active = False
        self.timer = 0

    def draw_wall(self):
        if self.active:
            wall_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), self.w, self.h)
            pygame.draw.rect(screen, GREY, wall_rect)

    def activate_wall(self):
        self.active = True
        self.randomize_position()
        self.randomize_size()
        self.timer = pygame.time.get_ticks()

    def deactivate_wall(self):
        self.active = False

    def update(self):
        if self.active and pygame.time.get_ticks() - self.timer > 5000:
            self.deactivate_wall()

    def randomize_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def randomize_size(self):
        self.w = random.randint(cell_size * 2, cell_size * 4)
        self.h = random.randint(cell_size, cell_size * 3)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        head_color = (255, 255, 255)  # White color
        head = self.body[0]
        x_pos = int(head.x * cell_size)
        y_pos = int(head.y * cell_size)
        head_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen, head_color, head_rect)

        for block in self.body[1:]:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, ORANGE, block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, RED, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    #.
    


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.wall = WALL()
        self.wall_timer = 0

    def update(self):
        self.snake.move_snake()
        self.wall.update()
        self.check_collisions()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.wall.draw_wall()

    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        elif self.wall.active and self.wall.pos == self.snake.body[0]:
            self.game_over()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

GREEN = (78, 186, 20)
RED = (217, 56, 56)
ORANGE = (248, 252, 3)
GREY = (105, 98, 92)
BLACK = (0,0,0)
#not sure
bg = pygame.image.load(r'C:\Users\Kamila\Pictures\Saved Pictures\bg.jpeg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    if pygame.time.get_ticks() - main_game.wall_timer > 10000:
        main_game.wall.activate_wall()
        main_game.wall_timer = pygame.time.get_ticks()

    #screen.fill(GREEN)
    #not sure
    screen.blit(bg, (0,0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
