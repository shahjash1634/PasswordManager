from Password_Manager.user._db_manager import store_password, show_details, delete_password

def menu():
    """
    Display a menu with options for the user.

    Returns:
    - str: User's choice input
    """
    print("""
        1. Store Password
        2. Show Details
        3. Delete Password
        4. Exit
        """)
    return input(" :")

def save_password():
    """
    Function to save a new password by taking input from the user.

    The user is prompted to enter information such as website, URL, username, email, password, and description.
    The entered information is then passed to the store_password function.
    """
    print(f"\nWebsite:  URL:   Username:    Email:   Password:   ")
    website = input('\n Website:')
    print(f"\nWebsite: {website} URL:   Username:    Email:   Password:  ")
    url = input('\n URL:')
    print(f"\nWebsite: {website}  URL:{url}   Username:    Email:   Password:  ")
    username = input('\n Username:')
    print(f"\nWebsite:{website}  URL: {url}  Username: {username}   Email:   Password:   ")
    email = input('\n Email:')
    print(f"\nWebsite:{website}  URL: {url}  Username: {username}  Email:{email}   Password:   ")
    password = input('\n Password:')
    print(f"\nWebsite:{website}  URL:{url}   Username:{username}    Email: {email} Password: {password}")
    description = input('\n Description:')
  
    store_password(website, url, username, email, password, description)

def remove_password():
    """
    Function to remove a password entry based on user input.

    The function displays details using show_details, prompts the user for the ID to delete,
    and asks for confirmation before calling delete_password.
    """
    show_details()
    for i in range(0,100):
        if del_id!=i:
            print("id does not exist")
    del_id = input("\n [-] Id That you want to delete: ")
    warn_check = input("Are you sure (y/n):")
    if warn_check == "y" or warn_check == "Y":
        delete_password(del_id)
        print("\n[-] Successfully deleted")
    else:
        print("\n[+] Cancelled Successfully")

def show_entries():
    """
    Function to display all password entries stored in the database using show_details.
    """
    show_details()

