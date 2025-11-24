import json

def save_file(accounts):
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)
        print("Data saved successfully!")

def load_file():
    try:
        with open("accounts.json", "r") as f:
            return json.load(f)
    except:
        return {}
