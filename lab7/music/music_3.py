import pygame

pygame.init() 
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 620
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

beatles = pygame.mixer.Sound(r'C:\Users\Kamila\Music\music for pp2\The_Beatles.mp3')
queen = pygame.mixer.Sound(r'C:\Users\Kamila\Music\music for pp2\Queen.mp3')
radiohead = pygame.mixer.Sound(r'C:\Users\Kamila\Music\music for pp2\Radiohead.mp3')
lana_del_rey = pygame.mixer.Sound(r'C:\Users\Kamila\Music\music for pp2\Lana_Del_Rey.mp3')
victor_tsoi = pygame.mixer.Sound(r'C:\Users\Kamila\Music\music for pp2\Victor_Tsoi.mp3')

music_arr = [beatles, queen, radiohead, lana_del_rey, victor_tsoi]

beatles_photo = pygame.image.load(r'C:\Users\Kamila\Pictures\pp2_photos\beatles_photo.jpg')
queen_photo = pygame.image.load(r'C:\Users\Kamila\Pictures\pp2_photos\Queen_photo.jpg')
radiohead_photo = pygame.image.load(r'C:\Users\Kamila\Pictures\pp2_photos\radiohead_photo.jpg')
lana_del_rey_photo = pygame.image.load(r'C:\Users\Kamila\Pictures\pp2_photos\lana_photo.jpg')
victor_tsoi_photo = pygame.image.load(r'C:\Users\Kamila\Pictures\pp2_photos\tsoi_photo.jpg')

# Adjusting photo positions
beatles_x = (SCREEN_WIDTH - 402) // 2
lana_del_rey_x = (SCREEN_WIDTH - 398) // 2
queen_x = 0  # Already full width
radiohead_x = (SCREEN_WIDTH - 410) // 2
victor_tsoi_x = (SCREEN_WIDTH - 452) // 2

photo_arr = [beatles_photo, queen_photo, radiohead_photo, lana_del_rey_photo, victor_tsoi_photo]
photo_positions = [beatles_x, queen_x, radiohead_x, lana_del_rey_x, victor_tsoi_x]

current_song_index = 0

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_arr)
    pygame.mixer.stop()
    music_arr[current_song_index].play()

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_arr)
    pygame.mixer.stop()
    music_arr[current_song_index].play()

running = True
is_playing = False

while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.pause()
                    is_playing = False
                else:
                    pygame.mixer.unpause()
                    is_playing = True
            elif event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()

    screen.fill((255, 255, 255))
    screen.blit(photo_arr[current_song_index], (photo_positions[current_song_index], 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
