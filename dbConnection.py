import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", 
  database="task"
)

def getData():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM table_product")
  myresult = mycursor.fetchall()
  print (myresult)
  return myresult
