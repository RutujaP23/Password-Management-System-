# 🔐 Password Management System (Python + SQLite)

A simple **CLI-based Password Management System** built using **Python**, **SQLite**, and **Fernet encryption**.
This project demonstrates secure password storage, encryption/decryption, and basic database operations.

---

## 📌 Features

* Add users with **encrypted passwords**
* Retrieve and decrypt stored passwords
* View all registered users
* Uses **SQLite** for persistent storage
* Menu-driven **Command Line Interface (CLI)**
* Prevents SQL Injection using parameterized queries

---

## 🛠️ Technologies Used

* **Python 3**
* **SQLite3**
* **cryptography (Fernet)**
* Standard Python libraries

---

## 📂 Project Structure

```
password-manager/
│
├── password_manager.py     # Main application file
├── password_manager.db     # SQLite database (auto-generated)
├── secret.key              # Encryption key (auto-generated)
├── README.md               # Project documentation
```

---

## ⚙️ How It Works

1. A **secret encryption key** is generated once and stored securely.
2. User passwords are **encrypted using Fernet symmetric encryption**.
3. Encrypted passwords are stored in an SQLite database.
4. When requested, passwords are decrypted using the same key.

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Library

```bash
pip install cryptography
```

### 2️⃣ Run the Program

```bash
python password_manager.py
```

---

## 📋 Menu Options

```
1. Add User
2. Get Password
3. Show All Users
4. Exit
```

---

## 🔒 Security Notes

* Passwords are stored in **encrypted form**, not plain text.
* Encryption key is stored locally (`secret.key`) and reused to allow decryption.
* For real-world applications:

  * Password **hashing (bcrypt/argon2)** is recommended instead of encryption
  * Passwords should never be displayed in plaintext

---

## 🎯 Use Case

This project is suitable for:

* College **mini project**
* Python fundamentals demonstration
* Learning **SQLite + cryptography**
* Internship or academic portfolio

---

## 📈 Future Enhancements

* Replace encryption with **password hashing**
* Add **user authentication (login system)**
* Build a **GUI using Tkinter**
* Convert into a **Flask / FastAPI backend**
* Store encryption keys using **environment variables**

---

## 👩‍💻 Author

**Rutuja Anandrao Patil**
Computer Engineering Student
Python | Android | SQL | Machine Learning

---

## 📄 License

This project is for **educational purposes only**.

---

