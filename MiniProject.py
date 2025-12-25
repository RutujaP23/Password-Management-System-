import sqlite3
from cryptography.fernet import Fernet

# Generate a key for encryption
# IMPORTANT: Save this key in a secure location
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Connect to SQLite database
conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

# Create a table for users if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Function to add a user with encrypted password
def add_user(username, password):
    # Encrypt the password
    encrypted_password = cipher_suite.encrypt(password.encode())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, encrypted_password))
        conn.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")

# Function to retrieve and decrypt password
def get_password(username):
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result:
        encrypted_password = result[0]
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        print(f"Password for {username}: {decrypted_password}")
    else:
        print("User not found.")

# Function to display all users (for demonstration purposes)
def show_all_users():
    cursor.execute("SELECT id, username FROM users")
    for user in cursor.fetchall():
        print(user)

# Main program logic
def main():
    while True:
        print("\nPassword Management System")
        print("1. Add User")
        print("2. Get Password")
        print("3. Show All Users")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif choice == '2':
            username = input("Enter username to retrieve password: ")
            get_password(username)
        elif choice == '3':
            show_all_users()
        elif choice == '4':
            print("Exiting Password Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
    # Close database connection when done
    conn.close()
