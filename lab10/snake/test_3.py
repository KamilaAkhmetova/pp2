import pygame as pg
import psycopg2
from random import randrange

# Database setup
connection = psycopg2.connect(host="localhost", dbname="snake", user="postgres",
                           password="ppluchsiypredmet)", port=5432)
c = connection.cursor()
# Create tables
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    level INT
);
""")
c.execute("""CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    score INT
);
""")

pg.init()

w, h, fps, step = 800, 800, 6, 40
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Snake Game')
is_running, lose = True, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390), pg.SRCALPHA)
bg = pg.image.load("bg.jpeg")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load("game_over.jpg")
gameover = pg.transform.scale(gameover, (390, 390))

class Food:
    def __init__(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.pic = pg.image.load("cherry.png")

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

    def draw2(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)

class Snake:
    def __init__(self):
        self.speed = step
        self.body = [[360, 360]]
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = 'green'
        self.width = w
        self.height = h
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.dx == 0:
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_RIGHT and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_UP and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_DOWN and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

    def draw(self):
        # Draw the head separately with white color
        head_x, head_y = self.body[0]
        pg.draw.rect(screen, 'white', (head_x, head_y, step, step))

        # Draw the rest of the body
        for part in self.body[1:]:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))

    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.score += 1
            self.body.append([1000, 1000]) 
    
    def self_collide(self):
        global is_running
        head_x, head_y = self.body[0]
        # Check collision with screen borders
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            is_running = False
        # Check self-collision
        if self.body[0] in self.body[1:]:
            is_running = False

    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body:
            f.draw2()

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("wall.png")

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

# Function to create or retrieve user
def create_or_get_user(username):
    c.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = c.fetchone()
    if user:
        print(f"Welcome back, {username}!")
        print(f"Current level: {user[2]}")
        return user
    else:
        c.execute("INSERT INTO users (username, level) VALUES (%s, %s)", (username, 0))
        connection.commit()
        print(f"Welcome, {username}!")
        return (c.lastrowid, username, 0)

# Function to save user score
def save_score(user_id, score, level):
    try:
        # Update user's level
        c.execute("UPDATE users SET level=%s WHERE id=%s", (level, user_id))
        # Insert user's score
        c.execute("INSERT INTO user_scores (user_id, score) VALUES (%s, %s)", (user_id, score))
        # Commit changes
        connection.commit()
        print("Score and level updated successfully.")
    except Exception as e:
        print("Error:", e)
        connection.rollback()

# Get username from user
username = input("Enter your username: ")
current_user = create_or_get_user(username)
user_id, _, level = current_user

# Game setup
s = Snake()
f = Food()

while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False

    screen.blit(bg, (0, 0))

    # Calling methods
    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.self_collide()
    s.check_food(f)

    # Display current score and level
    counter = score.render(f'Score: {s.score}', True, 'black')
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    # Check for level up
    if s.score == 3:
        level += 1
        level %= 4 
        fps += 2
        s.score = 0

    # Game over loop
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False   
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (320, 405))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (322, 435))
        pg.display.flip()

        # Update database with user's score and level
        save_score(user_id, s.score, level)

    # Save game state shortcut (Ctrl + S)
    keys = pg.key.get_pressed()
    if keys[pg.K_s] and (keys[pg.K_LCTRL] or keys[pg.K_RCTRL]):
        save_score(user_id, s.score, level)
        print("Game state saved.")

    pg.display.flip()

# Close the database connection
connection.close()
pg.quit()
