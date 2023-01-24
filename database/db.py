import mysql.connector

_db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sma"
)

cursor = _db_conn.cursor()

def createUsersTable():
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `users`(
                `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                `fullname` VARCHAR(300) NOT NULL,
                `email` VARCHAR(300) UNIQUE NOT NULL,
                `username` VARCHAR(300) UNIQUE NOT NULL,
                `password` VARCHAR(300) NOT NULL,
                `gender` ENUM("male", "female", "others"),
                `date_created` TIMESTAMP
            )
         """)

def createNotesTable():
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `notes`(
                `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                `author_id` INT NOT NULL,
                `note_title` LONGTEXT NOT NULL,
                `note_content` LONGTEXT NOT NULL,
                `date_created` TIMESTAMP
            )
         """)


def checkIfUserExists(username, password):
    cursor.execute("SELECT * FROM `users` WHERE `username` = '"+ username + "' AND `password` ='" +password + "' LIMIT 1")
    for result in cursor:
        if result is not None:
            return result
    else:
        return None

def registerUser(fullname, email, username, gender, password):
    pass

def loginUser():
    username = input("Enter your username: ")
    password = input("Enter your password: ")  
    result = checkIfUserExists(username, password) 
    return result