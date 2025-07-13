# 🔐 Password Manager

A simple, terminal-based password manager built using **Python** and **MySQL**. This project lets users securely store, view, and manage login credentials (username, password, and associated website). Designed as a beginner-level project to demonstrate database handling and basic CRUD operations.

---

## 📦 Features

- ✅ Add new login credentials
- 📋 View all saved credentials
- 🔍 Search credentials by username
- ❌ Delete specific entries
- 🧹 Clear the entire password database
- 🛠️ Error handling for invalid inputs

---

## 🛠️ Tech Stack

- **Python 3**
- **MySQL Connector for Python**
- **MySQL Database**

---

## 🗃️ Table Structure

Database: `sam`  
Table: `password_manager`

| Column   | Type         | Constraints      |
|----------|--------------|------------------|
| Username | VARCHAR(100) | NOT NULL         |
| Password | VARCHAR(100) | NOT NULL         |
| Website  | VARCHAR(150) | NOT NULL         |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Password-Manager.git
cd Password-Manager
```

### 2. Set Up MySQL

- Create a database named ```sam```

- Ensure your MySQL root user has username ```root``` and password ```root```

- You can change these credentials in the script if needed

### 3. Install Requirements

```pip install mysql-connector-python```

### 4. Run the Script

``` python password_manager.py ```

### 💡 Usage

When you run the script, a simple menu will appear:

```Welcome to password manager :)

Press 1 to add your details
Press 2 to display all your details
Press 3 to view particular details
Press 4 to delete particular details
Press 5 to clear all details
Press 6 to exit password manager
```

Input the number corresponding to the action you'd like to perform.

### 🧑‍💻 Author

[@keerthiparam](https://www.github.com/keerthiparam)

Note: This is a learning project and should not be used to store real passwords without encryption and security best practices.

---
