import mysql
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Libraries4Life!",
    database="test"
)

cursor = db_connection.cursor

if db_connection.is_connected():
    print("Connected")

    db_connection.close()