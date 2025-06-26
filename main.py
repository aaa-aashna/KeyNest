import json
import os
import subprocess

DATA_FILE = "password.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def encrypt(password):
    result = subprocess.run(["./keynest_encryptor", "encrypt", password], capture_output=True, text=True)
    return result.stdout.strip()

def decrypt(encrypted):
    result = subprocess.run(["./keynest_encryptor", "decrypt", encrypted], capture_output=True, text=True)
    return result.stdout.strip()

def add_password(data):
    key = input("Enter the key (e.g., Gmail, GitHub): ")
    password = input("Enter the password: ")
    encrypted = encrypt(password)
    data[key] = encrypted
    save_data(data)
    print("Password added successfully.")

def view_all_passwords(data):
    if not data:
        print("No passwords saved.")
        return
    print("Stored Passwords:")
    for key, encrypted in data.items():
        decrypted = decrypt(encrypted)
        print(f" - {key}: {decrypted}")

def search_password(data):
    key = input("Enter the key to search: ")
    if key in data:
        decrypted = decrypt(data[key])
        print(f"Found: {key} -> {decrypted}")
    else:
        print("Key not found.")

def delete_entry(data):
    key = input("Enter the key to delete: ")
    if key in data:
        del data[key]
        save_data(data)
        print(f"'{key}' deleted.")
    else:
        print("Key not found.")

def menu():
    data = load_data()
    while True:
        print("\nKeyNest Password Manager")
        print("Choose your operation:")
        print("1. Add New Password")
        print("2. View All Passwords")
        print("3. Search Password")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == '1':
            add_password(data)
        elif choice == '2':
            view_all_passwords(data)
        elif choice == '3':
            search_password(data)
        elif choice == '4':
            delete_entry(data)
        elif choice == '5':
            print("Exiting KeyNest...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
