import psycopg2

conn = psycopg2.connect(
    database="lab10",
    user='postgres',
    password='3951925kamila',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

# CSV to TABLE
f = open("phonenumbers.csv", "r")
cursor.copy_from(f, 'phonebook', sep=',')
f.close()

# Insert entering user name, phone from console
first = input("Name: ")
num = input("Num: ")  # Assuming the phone number is entered as a string

postgres_insert_query = """INSERT INTO phonebook(first_name, phone_num) VALUES (%s, %s)"""
record_to_insert = (first, num)
cursor.execute(postgres_insert_query, record_to_insert)

conn.commit()
print("Successfully inserted!")
conn.close()
