import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    
    screen.fill((0, 0, 0))  # Fill the screen with black to clear the previous drawings
    
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    
    pygame.draw.rect(screen, color, pygame.Rect(3, 70, 60, 40))# first coordinates, then parameteres of rectangular
    
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

pygame.quit()
