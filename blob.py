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

def InsertBlob(FilePath, title, description, price, availability):
    inserQuery = """INSERT INTO table_product(title, description, price, photo, availability) value(%s,%s,%s,%s,%s)"""
    convertpic = convert_to_binary(FilePath)
    value = (title, description, price, convertpic, availability)
    mycursor.execute(inserQuery, value)
    mydb.commit()


def RetrieveBlob (ID):
    #convertfile = binary_to_file(filename)
    SqlStatement2 ="SELECT * FROM table_product "#WHERE id='{ID}'"
    mycursor.execute(SqlStatement2.format(str(ID)))
    myresult = mycursor.fetchall()[1]
    StoreFilePath = "imageoutput/img{0}.jpg".format(str(ID))
    print (myresult)
    with open(StoreFilePath,'wb') as File:
        File.write(myresult)
        File.close()

def EditBlob(id, FilePath, title, description, price, availability):
    updateQuery = """ UPDATE table_product SET title=%s, description=%s, price=%s, photo=%s, availability=%s where id=id """
    convertpic = convert_to_binary(FilePath)
    value = (3, 'Rock', 'Headbangers', 'Rs.1000', convertpic, 5)
    mycursor.execute(updateQuery, value)
    mydb.commit()


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
    title = str(input("Enter the title for your post: "))
    description = str(input("Enter the description of your post: "))
    price = str(input("Enter the price for your post: "))
    availability = str(input("Enter the availability for your post: "))
    UserFilePath = input("Insert Photo Path: ")
    InsertBlob(UserFilePath, title, description, price, availability)
elif int(menuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetrieveBlob(UserIDChoice)
