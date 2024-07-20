from cryptography.fernet import Fernet
import os


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    if not os.path.exists("key.key"):
        generate_key()
    return open("key.key", "rb").read()


def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password


def save(site, username, password, key):
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{site},{username},{encrypted_password.decode()}\n")
    print(f"Password for {site} saved successfully.")


def retrieve(site, key):
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                stored_site, stored_username, stored_encrypted_password = (
                    line.strip().split(",")
                )
                if stored_site == site:
                    try:
                        decrypted_password = decrypt_password(
                            stored_encrypted_password.encode(), key
                        )
                        print(
                            f"Site: {stored_site}, Username: {stored_username}, Password: {decrypted_password}"
                        )
                        return
                    except Exception as e:
                        print(f"Failed to decrypt password for {site}: {e}")
                        return
        print(f"No password found for the site: {site}.")
    except FileNotFoundError:
        print("No passwords stored yet. Please save a password first.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    key = load_key()
    while True:
        choice = input(
            "\nDo you want to (1) Save a password or (2) Retrieve a password? Enter 1 or 2: "
        )
        if choice == "1":
            site = input("Enter the site: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            save(site, username, password, key)
        elif choice == "2":
            site = input("Enter the site to retrieve the password: ")
            retrieve(site, key)
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
