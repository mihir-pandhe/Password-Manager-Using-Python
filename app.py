def save(site, username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{site},{username},{password}\n")
    print("Password saved successfully.")

def retrieve(site):
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                stored_site, stored_username, stored_password = line.strip().split(",")
                if stored_site == site:
                    print(f"Site: {stored_site}, Username: {stored_username}, Password: {stored_password}")
                    return
        print("No password found for the given site.")
    except FileNotFoundError:
        print("No passwords stored yet.")

def main():
    while True:
        choice = input("Do you want to (1) Save a password or (2) Retrieve a password? Enter 1 or 2: ")
        if choice == "1":
            site = input("Enter the site: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            save(site, username, password)
        elif choice == "2":
            site = input("Enter the site to retrieve the password: ")
            retrieve(site)
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
