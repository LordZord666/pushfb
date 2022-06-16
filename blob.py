import mysql.connector
import os
from dbConnection import postData
from mysqlx import sqlstatement

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database ="task"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Images(id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

def InsertBlob(FilePath):
    print(FilePath)
    with open(FilePath,"rb") as File:
        BinaryData = File.read()
    SqlStatement = "INSERT INTO Images (Photo) VALUES (%)"
    mycursor.execute(SqlStatement, BinaryData)
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


def TestBlob(FilePath):
    with open(FilePath,"rb") as File:
        BinaryData = File.read()
        # print(BinaryData)
        insert_blob_query = f"""
        INSERT INTO images(image) VALUES (%s);
        """
        data_tuple = (FilePath, BinaryData)
        # x = postData(data_tuple)
        # print(x)

        result = mycursor.execute(insert_blob_query, data_tuple)
        print(result)
        mydb.commit()
        print('File inserted successfully')
        mycursor.close()
        mydb.close()

        # print(data_tuple)

        # mycursor.execute(insert_blob_query, data_tuple)
        # mydb.commit()


    #     # Execute the query
    #     mycursor.execute(insert_blob_query, data_tuple)
    #     mydb.commit()
    #     print('File inserted successfully')
    #     mycursor.close()
    # except error.sql as error:
    #     print("Failed to insert blob into the table", error)
    # finally:
    #     if mydb:
    #         mydb.close()
    #         print("Connection closed")

print("1. Insert image\n2. Read image")
menuInput = input()

if int(menuInput) == 1:
    UserFilePath = input("Enter file path")
    # InsertBlob(UserFilePath)
    TestBlob(UserFilePath)
elif int(menuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetrieveBlob(UserIDChoice)

