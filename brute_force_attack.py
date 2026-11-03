def brute_force(passwd_list, correct_passwd):

    for passwd in passwd_list:
        print(f"Trying to get: {passwd.strip()}")

        if passwd.strip() == correct_passwd:
            print(f"Password has been found: {passwd.strip()}")
            return true

    print("Password not found")

    return false


# Read whole password from an existed file dicts

passwd_list = "passwd_list.txt"

try:
    with open(passwd_list, "r") as file:
        password_list = file.readlines()

    # standard user input
    correct_password = input("Type a password to check: ")

    brute_force(password_list, correct_password)
except FileNotFoundError:
    print("Stated file not found!")