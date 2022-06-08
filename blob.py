import mysql.connector
from mysqlx import SqlStatement

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database ="task"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Images(id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

def InsertBlob(FilePath):
    with open(FilePath,"rb") as File:
        BinaryData = File.read()
    SqlStatement = "INSERT INTO Images (Photo) VALUES (%)"
    mycursor.execute(SqlStatement, (BinaryData , ))
    mydb.commit()

def RetrieveBlob (ID):
    SqlStatement2 ="SELECT * FROM Images WHERE id='{0}'"
    mycursor.execute(SqlStatement2.format(str(ID)))
    myresult = mycursor.fetchall()[1]
    StoreFilePath = "imageoutput/img{0}.jpg".format(str(ID))
    print (myresult)
    with open(StoreFilePath,'wb') as File:
        File.write(myresult)
        File.close()

print("1. Insert image\n 2. Read image")
menuInput = input()

if int(menuInput) == 1:
    UserFilePath = input("Enter file path")
    InsertBlob(UserFilePath)
elif int(menuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetrieveBlob(UserIDChoice)