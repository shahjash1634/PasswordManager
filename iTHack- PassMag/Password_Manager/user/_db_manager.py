
from Password_Manager.user._user_db import connect_database
import prettytable as PrettyTable

def store_password(website, url, username, email, password, description):
    """
    Function to store a new password entry in the database.

    Parameters:
    - website: Website name (str)
    - url: Website URL (str)
    - username: Username for the website (str)
    - email: Email associated with the account (str)
    - password: Password for the account (str)
    - description: Additional description or notes (str)
    """
    conn = connect_database()
    myCur = conn.cursor()

    sqlQuery = "INSERT INTO UserDataBase (Website, URL, Username, Email, Password, Description) VALUES(?, ?, ?, ?, ?, ?)"
    val = (website, url, username, email, password, description)
    myCur.execute(sqlQuery, val)

    conn.commit()
    conn.close()

def delete_password(acc_id):
    """
    Function to delete a password entry from the database based on the given account ID.

    Parameters:
    - acc_id: Account ID to be deleted (int)
    """
    conn = connect_database()
    myCur = conn.cursor()
    sqlQuery = "DELETE FROM UserDataBase WHERE Id=?"
    accToDelete = (acc_id,)
    if accToDelete.count==0:
        print("[-] Invalid ID")
    
    myCur.execute(sqlQuery, accToDelete)
    conn.commit()
    conn.close()
    print("[-] Record deleted")

def show_details():
    """
    Function to display all password entries stored in the database in a tabular format.
    """
    conn = connect_database()
    myCur = conn.cursor()
    sqlQuery = "SELECT Id, Website, URL, Username, Email, Password, Description FROM UserDataBase"

    myCur.execute(sqlQuery)
    rows = myCur.fetchall()

    myTable = PrettyTable.PrettyTable(["Id", "Website", "URL", "Username", "Email", "Password", "Description"])
    for row in rows:
        myTable.add_row(row)
    print(myTable)

def clear_data():
    """
    Function to clear all records from the database.
    """
    conn = connect_database()
    myCur = conn.cursor()
    sqlQuery = "DELETE FROM UserDataBase"
    myCur.execute(sqlQuery)
    conn.commit()
    conn.close()
    print("[-] All records cleared")

