import hashlib

def accounts_data():
    accounts = {}

    while True:
        account_name = input("Enter your account name ('Done' to finish or 'Exit' to quit): ").strip()
        if account_name.capitalize() == 'Exit':
            print("The program is closed, see you next time.")
            break
        if account_name.capitalize() == 'Done':
            break
        if account_name == "":
            print("Please enter a valid account name.")
            continue

        while True:
            user_name = input(f"Enter the username used on {account_name}: ").strip()
            if user_name != "":
                break
            print("Please enter a valid username.")

        while True:
            password = input(f"Enter your password for {account_name}: ").strip()
            if password == "":
                continue
            if len(password) < 10:
                print("The password should be at least 10 characters")
                continue
            break  

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        accounts[account_name] = {"username": user_name, "password": hashed_password}
        print(f"Account '{account_name}' added successfully!\n")

    return accounts
