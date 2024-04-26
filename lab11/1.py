import psycopg2

conn = psycopg2.connect(
  database="lab10",
  user='postgres',
  password='3951925kamila',
  host='localhost',
  port='5432'
)


cursor = conn.cursor()

name = str(input("name: "))
select_query = f"select phone_num from phonebook where first_name = '{name}'"
cursor.execute(select_query)
result = cursor.fetchone()
print(result[0])