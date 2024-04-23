#Implement deleting data from tables by username of phone
import psycopg2

conn = psycopg2.connect(
	database="lab10",
	user='postgres',
	password='ppluchsiypredmet)',
	host='localhost',
	port='5432'
)
cursor = conn.cursor()
conn.autocommit = True


#looking with the first and last name
first_old = str(input("Enter first name of person, whom you want to delete: "))

sql = f"select * from phonebook where first_name =\'{first_old}\'"
cursor.execute(sql)
info = cursor.fetchall()


if len(info) > 0:
    sql_update = f"Delete from phonebook where  first_name =\'{first_old}\'; " 
    cursor.execute(sql_update)
    print("successfully!")
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()