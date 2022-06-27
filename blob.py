import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database ="task"
)

mycursor = mydb.cursor()

def InsertBlob(FilePath, title, description, price, availability):
    insertQuery = """INSERT INTO table_product(title, description, price, photo, availability) value(%s,%s,%s,%s,%s)"""
    convertpic = convert_to_binary(FilePath)
    value = (title, description, price, convertpic, availability)
    mycursor.execute(insertQuery, value)
    mydb.commit()


def RetrieveBlob(id):
    selectQuery = "SELECT * from images where id = '{0}'"
    mycursor.execute(selectQuery.format(str(id)))
    myresult = mycursor.fetchone()[2]
    StoreFilePath = "Image.Outputs/img{0}.jpg".format(str(id))
    print(myresult)
    sql_select_query = "SELECT * FROM images where id = '{0}'"
    mycursor.execute(selectQuery.format(str(id)))
    myresult1 = mycursor.fetchone()[1]
    StoreFilePath = "Image_Outputs/img{0}.jpg".format(str(id))
    print(myresult1)
    with open(StoreFilePath, 'wb') as file:
        file.write(myresult)
        file.close()


def EditBlob(id, FilePath, title, description, price, availability):
    with open(FilePath, "rb") as file:
        binary_data = file.read()
    updateQuery = """ UPDATE table_product SET title=%s, description=%s, price=%s, photo=%s, availability=%s where id=%s """
    value = (id, title, description, price, binary_data, availability)
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
        print(file)


print("1. Insert image\n2. Read image\n3. Update image")
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
elif int(menuInput) == 3:
    title = str(input("Enter the title for your post: "))
    description = str(input("Enter the description of your post: "))
    price = str(input("Enter the price for your post: "))
    availability = str(input("Enter the availability for your post: "))
    FilePath = input("Insert Photo Path: ")
    EditBlob(id, FilePath, title, description, price, availability)
