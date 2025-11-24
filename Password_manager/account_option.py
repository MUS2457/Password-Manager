def view_account(accounts):
    while True:
        account_name = input("Enter the account name to view ('DONE' to finish, 'EXIT' to quit): ").strip()

        if account_name.upper() == "EXIT":
            print("Exiting view accounts...")
            return None

        if account_name.upper() == "DONE":
            return None

        if account_name in accounts:
            account_info = accounts[account_name]
            return account_info   
        else:
            print(f"No account found with the name '{account_name}'\n")

import hashlib

def update_account(accounts) :
    while True:
        account_name = input("Enter the account name to view ('DONE' to finish, 'EXIT' to quit): ").strip()

        if account_name.upper() == "EXIT":
            print("Exiting update accounts...")
            return None
        if account_name.upper() == "DONE" :
            return None
        if account_name not in accounts :
            print("The account has not been found !,please try again.")
            continue

        choise = input("What would you like to update ? ('username' or 'password')").strip()
        
        if choise.lower() == 'username' :

            new_username = input("enter the new user name : ").strip()
            if new_username == "" :
                print("the username cannot be empty.try again")
                continue
            accounts[account_name]['username'] = new_username
            print("Username updated successfully!\n")
            return accounts
        
        elif choise.lower() == 'password' :

            new_password = input("Enter the new password : ").strip()
            if new_password == "" :
                print("the password cannot be empty.try again")
                continue
            if len(new_password) < 10 :
                print("Password too short. Must be at least 10 characters.")
                continue
            hash_pass = hashlib.sha256(new_password.encode()).hexdigest()
            accounts[account_name]['password'] = hash_pass
            print("Password updated successfully!\n")
            return accounts

        else:
            print("Invalid option. Type username or password.\n")


def delete_account(accounts):
    while True:
        account_name = input("Enter the account name to delete ('DONE' to finish, 'EXIT' to quit): ").strip()

        if account_name.upper() == "EXIT":
            print("Exiting delete accounts...")
            return None
        if account_name.upper() == "DONE":
            return None
        if account_name not in accounts:
            print("The account has not been found! Please try again.")
            continue

        delete = input("Would you like to delete? ('yes' or 'no'): ").strip().lower()

        if delete == 'yes':
            del accounts[account_name]
            print("The account was deleted successfully!\n")
            return accounts
        elif delete == 'no':
            print("Deletion canceled.\n")
            return None
        else:
            print("Invalid option. Type 'yes' or 'no'.\n")
