# 🔐 Secure Login System

A secure user authentication system built using **Python**, **Object-Oriented Programming (OOP)**, and **Bcrypt Password Hashing**. The application allows users to register and log in securely while storing hashed passwords in a JSON file.

---

## 📌 Features

- User Registration
- User Login Authentication
- Secure Password Hashing using Bcrypt
- Password Verification
- JSON-Based User Storage
- Object-Oriented Design
- Duplicate Username Detection
- Persistent User Data Storage
- Simple Command-Line Interface (CLI)

---

## 🛠️ Technologies Used

- Python 3
- Bcrypt
- JSON
- Object-Oriented Programming (OOP)
- File Handling

---

## 📂 Project Structure

```text
Secure login system/
│
├── main.py
├── users.json
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/secure-login-system.git
```

### 2. Navigate to Project Directory

```bash
cd secure-login-system
```

### 3. Create Virtual Environment (Optional)

```bash
python -m venv myenv
```

### Activate Virtual Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Mac/Linux

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```txt
bcrypt
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 💻 Example Usage

### Main Menu

```text
===== Secure Login System =====

1. Register
2. Login
3. Exit

Enter choice:
```

### Registration

```text
Enter choice: 1

Enter username: arshi
Enter password: admin123

Registration successful.
```

### Login

```text
Enter choice: 2

Enter username: arshi
Enter password: admin123

Login Successful
```

---

## 🔒 Password Security

Passwords are never stored in plain text.

Example:

### User Password

```text
admin123
```

### Stored Hash

```text
$2b$12$F4j3sGdK8nA9....
```

This improves security and protects user credentials.

---


---

## 🧠 Concepts Demonstrated

### Python Fundamentals
- Variables
- Functions
- Loops
- Conditions

### Object-Oriented Programming
- Classes
- Objects
- Methods
- Constructors

### File Handling
- Reading JSON Files
- Writing JSON Files

### Security Concepts
- Password Hashing
- Authentication
- User Validation

### Error Handling
- Invalid User Detection
- Duplicate Username Prevention

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

- How authentication systems work
- How password hashing improves security
- How to use Bcrypt in Python
- How to implement OOP in real-world applications
- How to persist data using JSON files
- How login systems validate user credentials

---

## 🔮 Future Improvements

- Password Strength Validation
- Hidden Password Input using `getpass`
- Forgot Password Functionality
- Login Attempt Limiter
- Activity Logging
- SQLite Database Integration
- User Roles (Admin/User)
- Email OTP Verification
- Flask Web Version
- JWT Authentication

---

## 📸 Sample Output

```text
===== Secure Login System =====

1. Register
2. Login
3. Exit

Enter choice: 1

Enter username: arshi
Enter password: admin123

Registration successful.
```

```text
===== Secure Login System =====

1. Register
2. Login
3. Exit

Enter choice: 2

Enter username: arshi
Enter password: admin123

Login Successful
```

---

## 👨‍💻 Author
Arsheen Shaikh
---

