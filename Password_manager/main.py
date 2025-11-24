from account_data import accounts_data
from account_option import view_account, update_account, delete_account
from data_hundling import save_file, load_file
from datetime import datetime
import json

accounts = load_file()  

# If no accounts, let the user add new ones
if not accounts:
    print("No accounts found. Let's add some!")
    accounts = accounts_data()

while True:
    user_choice = input("Choose one ('view', 'update', 'delete', 'exit'): ").strip().lower()

    if user_choice == "view":
        info = view_account(accounts)
        if info:
            print(f"\nUsername: {info['username']}")
            print(f"Hashed Password: {info['password']}\n")

    elif user_choice == "update":
        updated_accounts = update_account(accounts)
        if updated_accounts:
            accounts = updated_accounts

    elif user_choice == "delete":
        updated_accounts = delete_account(accounts)
        if updated_accounts:
            accounts = updated_accounts

    elif user_choice == "exit":
        print("Exiting program... Goodbye!")
        save_file(accounts)

        # Save a readable TXT report
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("report.txt", "w") as f:
            f.write(f"Accounts Report - Generated at {now}\n\n")
            for account, info in accounts.items():
                f.write(f"Account: {account}\n")
                f.write(f"  Username: {info['username']}\n")
                f.write(f"  Hashed Password: {info['password']}\n\n")
        print("TXT report saved successfully.\n")
        break

    else:
        print("Invalid choice. Try again.\n")
