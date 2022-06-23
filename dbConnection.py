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


# def postData(data_tuple):
#   mycursor = mydb.cursor()
#   mycursor.execute("INSERT INTO table_product(photo) VALUES(?);", data_tuple)
#   myresult = mycursor.commit()
#   print (myresult)
#   return myresult
