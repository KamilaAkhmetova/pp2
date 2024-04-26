import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    database="lab10",
    user='postgres',
    password='3951925kamila',
    host='localhost',
    port='5432'
)

# Create a cursor object using the connection
cursor = conn.cursor()

# Prompt the user for input
name = input("Enter user's name: ")
phone_num = input("Enter user's phone number: ")

# Check if the user already exists in the phonebook
cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
existing_user = cursor.fetchone()

if existing_user:
    # Update the phone number if the user exists
    cursor.execute("UPDATE phonebook SET phone_num = %s WHERE first_name = %s", (phone_num, name))
    print("User's phone number updated successfully!")
else:
    # Insert a new user if the user doesn't exist
    cursor.execute("INSERT INTO phonebook (first_name, phone_num) VALUES (%s, %s)", (name, phone_num))
    print("New user inserted successfully!")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
