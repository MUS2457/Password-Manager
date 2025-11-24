Features :

Add new accounts with username and password.

Passwords must be at least 10 characters long.

Passwords are hashed using SHA-256.

View account information (username and hashed password).

Update account username or password.

Delete existing accounts.

Save all account data automatically in a JSON file when exiting.

Load existing account data from JSON on program start.

Requirement :

No external libraries are needed — uses Python's standard hashlib and json.

Run the program:

python main.py

Follow on-screen prompts:

view — View account details

update — Update username or password

delete — Delete an account

exit — Exit and save all data
