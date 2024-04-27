import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="snake",
            user="postgres",
            password="ppluchsiypredmet)"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_tables(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS snakegame (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE
            );

            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id),
                score INT,
                level INT,
                game_state TEXT
            );
        """)
        conn.commit()
        cur.close()
        print("Tables created successfully.")
    except psycopg2.Error as e:
        print("Error creating tables:", e)

def register_or_get_user(conn):
    try:
        cur = conn.cursor()
        username = input("Enter your username: ")
        cur.execute("SELECT id, username FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        if user:
            print(f"Welcome back, {username}!")
            print(f"Your current level is {get_user_level(conn, user[0])}.")
            return user[0]  # Return user id
        else:
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"Welcome, {username}! You're a new player.")
            return user_id
    except psycopg2.Error as e:
        print("Error registering user:", e)
        return None

def get_user_level(conn, user_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
        level = cur.fetchone()
        return level[0] if level else 1  # Default level is 1 if no record found
    except psycopg2.Error as e:
        print("Error getting user level:", e)
        return None

def save_game_state(conn, user_id, score, level, game_state):
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO user_score (user_id, score, level, game_state) VALUES (%s, %s, %s, %s)",
            (user_id, score, level, game_state)
        )
        conn.commit()
        print("Game state saved successfully.")
    except psycopg2.Error as e:
        print("Error saving game state:", e)

def main():
    conn = connect_to_db()
    if conn:
        create_tables(conn)
        user_id = register_or_get_user(conn)
        # Assume the game has started and user reached a certain score and level
        score = 1000
        level = 5
        game_state = "Some game state data here..."
        save_game_state(conn, user_id, score, level, game_state)
        conn.close()

if __name__ == "__main__":
    main()
