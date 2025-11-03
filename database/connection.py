import mysql.connector as con 
try:
    #create connection 
    database = con.connect(host="localhost",user='root',passwd='',database='py27',port='3306')
    print('connection created.....')
except con.Error as error:
    print("Error in creating connection.")
    print(error)
