def groc_writer(grocery):
    with open('groceries.txt', "a") as file:
        file.write("\t".join(grocery) + "\n")


def read_groceries():
    with open('groceries.txt', "r") as file:
        groceries = file.read()
        print(groceries)


def read_admin_credentials():
    with open('credentials.txt', "r") as file:
        admin_credentials = file.read()
    return admin_credentials


def register():
    with open("credentials.txt", "a") as file:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        print("\nPlease choose  one of the roles as below: \n1. Admin \n2. Inventory-Checker \n3.Purchaser")
        choice = int(input("Enter a role: "))
        if choice == 1:
            role = "admin"
        elif choice == 2:
            role = 'inventory-checker'
        elif choice == 3:
            role = 'purchaser'
        else:
            print("Error. Invalid input")
        user_id = sum(1 for line in open('credentials.txt')) + 1
        file.write(str(user_id) + ' ' + username + ' ' + password + ' ' + role + '\n')
