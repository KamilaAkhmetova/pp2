import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.init() # CONST
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# width / height

MOVEMENT_SPEED = 20
CIRCLE_RADIUS = 25
INITIAL_X_POS = 100
INITIAL_Y_POS = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60

clock = pygame.time.Clock()

running = True

x = INITIAL_X_POS
y = INITIAL_Y_POS

# Main loop
while running:  
  # Getting all the events from OS
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pressed = pygame.key.get_pressed()

  if pressed[pygame.K_UP]:
    y = max(CIRCLE_RADIUS, y - MOVEMENT_SPEED)
  if pressed[pygame.K_DOWN]:
    y = min(SCREEN_HEIGHT - CIRCLE_RADIUS, y + MOVEMENT_SPEED)
  if pressed[pygame.K_LEFT]:
    x = max(CIRCLE_RADIUS, x - MOVEMENT_SPEED)
  if pressed[pygame.K_RIGHT]:
    x = min(SCREEN_WIDTH - CIRCLE_RADIUS, x + MOVEMENT_SPEED)

  screen.fill(WHITE)
  pygame.draw.circle(screen, RED, (x, y), CIRCLE_RADIUS)

  # Screen updating
  pygame.display.flip()
  clock.tick(FPS)