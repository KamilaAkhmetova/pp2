import pygame
import sys
from pygame.math import Vector2
import random

class WALL:
    #create wall class, wall appears randomly and dissapears after time(activates and diactivates)
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
#wall can appear in different size even like a rectangle or square
    def randomize_size(self):
        self.w = random.randint(cell_size * 2, cell_size * 4)
        self.h = random.randint(cell_size, cell_size * 3)


class SNAKE:
    def __init__(self):
        #there are specified initial coordinates for snake and its initial direction
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        #for more convenience i want to do head of the snake in white color while the snake itself in yellow(orange)
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
    #creating fruit class, actually it is just for apple
    #fruit as the wall appears randomly however it does not need to be activated or diactivated
    #also to create apple and pear i use blit because they are images
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class PEAR:
    #i wanted pear to act like a wall and to dissapear after time also pear gives more points
    def __init__(self):
        self.active = False
        self.timer = 0

    def draw_pear(self):
        if self.active:
            pear_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            screen.blit(pear, pear_rect)

    def activate_pear(self):
        self.active = True
        self.randomize_position()
        self.timer = pygame.time.get_ticks()

    def deactivate_pear(self):
        self.active = False

    def update(self):
        if self.active and pygame.time.get_ticks() - self.timer > 5000:
            self.deactivate_pear()

    def randomize_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.wall = WALL()
        self.pear = PEAR()
        self.pear_timer = 0
        self.wall_timer = 0
        self.score = 0
        self.level = 1
        self.fps = 8

    def update(self):
        self.snake.move_snake()
        self.wall.update()
        self.pear.update()
        self.check_collisions()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.wall.draw_wall()
        self.pear.draw_pear()
        self.draw_score()

    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.score += 1
        elif self.wall.active and self.wall.pos == self.snake.body[0]:
            self.game_over()
        elif self.pear.active and self.pear.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.score += 3

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = str(self.score)
        score_font = pygame.font.SysFont("Verdana", 20)
        score_surface = score_font.render(f'Score: {score_text}', True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("apple.png").convert_alpha()
pear = pygame.image.load("pear.png").convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

GREEN = (78, 186, 20)
RED = (217, 56, 56)
ORANGE = (248, 252, 3)
GREY = (105, 98, 92)
BLACK = (0, 0, 0)
bg = pygame.image.load('bg.jpeg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #applying key events to control movement of snake
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
    if pygame.time.get_ticks() - main_game.pear_timer > 10000:
        main_game.pear.activate_pear()
        main_game.pear_timer = pygame.time.get_ticks()

    # Level Up
    if main_game.score >= 3 * main_game.level:
        main_game.level += 1
        main_game.fps += 2

    screen.blit(bg, (0, 0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(main_game.fps)
