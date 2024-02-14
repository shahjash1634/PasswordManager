import tkinter as tk
import secrets
import string
from tkinter import simpledialog
from Password_Manager.user._db_manager import store_password, show_details, delete_password, clear_data

def generate_random_password(length=12):
    """
    Generate a random password with a specified length.

    Parameters:
    - length (int): Length of the generated password. Default is 12.

    Returns:
    - str: Randomly generated password.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password 

def save_password_gui():
    """
    Function to interactively save a new password using a graphical user interface.

    The user is prompted to enter information such as website, URL, username, email, and password.
    The option to generate a random password is also provided.
    The entered information is then passed to the store_password function.
    """
    website = simpledialog.askstring("Input", "Enter Website:")
    url = simpledialog.askstring("Input", "Enter URL:")
    username = simpledialog.askstring("Input", "Enter Username:")
    email = simpledialog.askstring("Input", "Enter Email:")
    
    # Ask if the user wants to generate a random password
    generate_password = simpledialog.askstring("Input", "Do you want to generate a random password? (y/n):")
    if generate_password.lower() == 'y':
        password = generate_random_password()
    else:
        password = simpledialog.askstring("Input", "Enter Password:")
    
    description = simpledialog.askstring("Input", "Enter Description:")
    
    store_password(website, url, username, email, password, description)

def remove_password_gui():
    """
    Function to interactively remove a password entry using a graphical user interface.

    The user is prompted to enter the ID of the password entry to be deleted,
    and confirmation is sought before calling the delete_password function.
    """
 
    del_id = simpledialog.askstring("Input", "Enter Id to delete:")
    for i in range(0,1):
        if del_id!=i:
            print("id does not exist")
    warn_check = simpledialog.askstring("Input", "Are you sure? (y/n):")
    
    if warn_check.lower() == "y":
        delete_password(del_id)
        print("\n[-] Successfully deleted")
    else:
        print("\n[+] Canceled Successfully")

def show_entries_gui():
    """
    Function to display all password entries stored in the database using a graphical user interface.
    """
    show_details()

def clear_data_gui():
    """
    Function to interactively clear all data from the database using a graphical user interface.

    Confirmation is sought before calling the clear_data function.
    """
    # Ask for confirmation before clearing all data
    confirm_clear = simpledialog.askstring("Input", "Are you sure you want to clear all data? This action cannot be undone. (y/n):")
    
    if confirm_clear.lower() == "y":
        clear_data()
        print("\n[-] All records cleared")
    else:
        print("\n[+] Clear Data Canceled")

def main_gui():
    """
    Main function to run the graphical user interface for the password manager.

    The user is presented with a menu to choose options like storing passwords, showing details, deleting passwords, clearing data, and exiting.
    The user can interactively perform these operations.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    while True:
        choose = simpledialog.askstring("Menu", "1. Store Password\n2. Show Details\n3. Delete Password\n4. Clear Data\n5. Exit\nEnter your choice:")
        
        if choose == "1":
            save_password_gui()
        elif choose == "2":
            show_entries_gui()
        elif choose == "3":
            remove_password_gui()
        elif choose == "4":
            clear_data_gui()
        elif choose == "5":
            break

if __name__ == "__main__":
    main_gui()
