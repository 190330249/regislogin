import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979")
mycursor=mydb.cursor()
#mycursor.execute("create database Project")
#mycursor.execute("Show Databases")
mycursor.execute("use Project")
mycursor.execute("create table Accounts(id int(12) NOT NULL AUTO_INCREMENT, username varchar(100),password varchar(100),email varchar(150),PRIMARY KEY(id))")