from fileinput import filename
from opcode import opname
import mysql.connector
import os
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
    inserQuery = """ INSERT INTO Images(id, photo) value(%s,%s)"""
    convertpic = convert_to_binary(FilePath)
    value = (1, convertpic)
    mycursor.execute(inserQuery, value)
    mydb.commit()


def RetrieveBlob (ID):
    # convertfile = binary_to_file(filename)
    SqlStatement2 ="SELECT * FROM Images WHERE id='{0}'"
    mycursor.execute(SqlStatement2.format(str(ID)))
    myresult = mycursor.fetchall()[1]
    StoreFilePath = "imageoutput/img{0}.jpg".format(str(ID))
    print (myresult)
    with open(StoreFilePath,'wb') as File:
        File.write(myresult)
        File.close()


# Convert Images to Binary
def convert_to_binary(filepath):
    with open(filepath, 'rb') as file:
        binarydata = file.read()
    return binarydata


# Convert binary_images to Files
def binary_to_file(filepath, binarydata):
    with open(filepath, 'wb') as file:
        file.write(binarydata)


print("1. Insert image\n2. Read image")
menuInput = input()

if int(menuInput) == 1:
    UserFilePath = input("Enter file path")
    InsertBlob(UserFilePath)
elif int(menuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetrieveBlob(UserIDChoice)

