import psycopg2

conn = psycopg2.connect(
	database="lab10",
	user='postgres',
	password='ppluchsiypredmet)',
	host='localhost',
	port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True

#looking with the first and last name
first_old = str(input("Enter first name that you want to change: "))
num_old = int(input("Enter first name that you want to change:  "))
sql = f"select * from phonebook where first_name =\'{first_old}\' and phone_num = \'{num_old}\' "
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
    new_first = str(input("Enter new name: "))
    new_phone = int(input("Enter new number: "))
    # im not sure!
    sql_update = f"Update phonebook set phone_num =\'{new_phone}\', first_name =\'{new_first}\' where first_name =\'{first_old}\'; " 
    cursor.execute(sql_update)
    print("successfully!")
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()