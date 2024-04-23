#Querying data from the tables (with different filters)
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

#select all
#sql = f"select * from phonebook";

#select filter 
#sql = f"select * from phonebook where first_name = \'Alua\' ";


#select with sort filter decrease by first
sql = f"select * from phonebook by order by first_name desc"


#select with sort filter increase by first
#sql = f"select * from phonebook by order by first_name asc";


cursor.execute(sql)
info = cursor.fetchall()
print(info)
