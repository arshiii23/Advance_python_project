import bcrypt
import json
import os


class SecureLoginSystem:

    def __init__(self):

        project_folder = os.path.dirname(os.path.abspath(__file__))

        self.file_name = os.path.join(project_folder, "users.json")

        self.users = self.load_users()

    def load_users(self):

        if not os.path.exists(self.file_name):

            with open(self.file_name, "w") as file:
                json.dump({}, file)

            return {}

        try:

            with open(self.file_name, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return {}

    def save_users(self):

        with open(self.file_name, "w") as file:
            json.dump(self.users, file, indent=4)

    def register(self):

        username = input("Enter username: ").strip()

        if username in self.users:
            print("User already exists.")
            return

        password = input("Enter password: ")

        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        self.users[username] = hashed_password.decode()

        self.save_users()

        print("Registration successful.")

    def login(self):

        username = input("Enter username: ").strip()

        password = input("Enter password: ")

        if username not in self.users:
            print("User not found.")
            return

        stored_hash = self.users[username].encode()

        if bcrypt.checkpw(password.encode(), stored_hash):
            print("Login Successful")
        else:
            print("Incorrect Password")

    def menu(self):

        while True:

            print("\n===== Secure Login System =====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("Goodbye")
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":

    app = SecureLoginSystem()
    app.menu()