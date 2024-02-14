import sqlite3
import os

def create_dbtable():
    """
    Function to create a table named 'Userdatabase' in the SQLite database if it does not exist.

    The table has the following columns:
    - Id: INTEGER PRIMARY KEY
    - Website: CHAR(50)
    - URL: TEXT(500)
    - Username: CHAR(50)
    - Email: TEXT(100)
    - Password: TEXT(100)
    - Description: TEXT(5000)
    """
    conn = sqlite3.connect("C:\\Users\\jashs\\OneDrive\\Desktop\\PasswordManager\\iTHack- PassMag\\Password_Manager\\user\\leveldb\\user.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Userdatabase
                   (Id INTEGER PRIMARY KEY,
                   Website CHAR(50),
                   URL TEXT(500),
                   Username CHAR(50),
                   Email TEXT(100),
                   Password TEXT(100),
                   Description TEXT(5000));''')
    conn.commit()
    conn.close()

def create_database():
    """
    Function to check if the directory and database file exist, and create them if not.

    The database file 'user.db' is created using the create_dbtable function.
    """
    if os.path.exists(r'C:\\Users\\jashs\\OneDrive\\Desktop\\PasswordManager\\iTHack- PassMag\\Password_Manager\\user\\leveldb\\'):
        if not os.path.exists(r"C:\\Users\\jashs\\OneDrive\\Desktop\\PasswordManager\\iTHack- PassMag\\Password_Manager\\user\\leveldb\\user.db"):
            create_dbtable()
    else:
        os.mkdir(r'C:\\Users\\jashs\\OneDrive\\Desktop\\PasswordManager\\iTHack- PassMag\\Password_Manager\\user\\leveldb')
        create_dbtable()

def connect_database():
    """
    Function to connect to the SQLite database and return the connection object.

    Returns:
    - conn: SQLite connection object
    """
    conn = sqlite3.connect(r"C:\\Users\\jashs\\OneDrive\\Desktop\\PasswordManager\\iTHack- PassMag\\Password_Manager\\user\\leveldb\\user.db")
    return conn

if __name__ == "__main__":
    create_database()
