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

# Alter the table schema to change the data type of the phone_num column to VARCHAR
alter_table_query = """
    ALTER TABLE phonebook 
    ALTER COLUMN phone_num TYPE VARCHAR(20);
"""

cursor.execute(alter_table_query)

conn.commit()
print("Successfully altered table schema!")
conn.close()
