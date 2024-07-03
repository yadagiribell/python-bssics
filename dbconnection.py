import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    password="giri@123",

)
mycur=conn.cursor()

if(mycur):
    print("success")
else:
    print("failed")

qurey="create table studentdb(name varchar(100),rollno varchar(100));"