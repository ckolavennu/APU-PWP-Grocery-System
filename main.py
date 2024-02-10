
# Import all the necessary modules and files


import filehandler as f
import admin as admin
import inventory_checker as ic
import purchaser

#This is the welcome message for the interface 
print("Welcome to APU Grocery Store")

while True:
    #This is for the login or registration page
    print("\nPress 1 to register, press 2 to login, press 0 to exit")
    choice = int(input("Choice: "))

    #Registration Process
    if choice == 1:
        f.register()
        while True:
            print("\nPress 1 to go to menu, press 0 to exit")
            menu_choice = int(input("Choice: "))
            if menu_choice == 1:
                break
            elif menu_choice == 0:
                exit()
            else:
                print("Invalid input. Try again.")

    #Login Process
    elif choice == 2:
        print("\t LOG IN")
        print("Please enter your username and password below: ")
        username = input("Username: ")
        password = input("Password: ")

        with open('credentials.txt', 'r') as f:
            for line in f:
                credentials = line.split()
                if credentials[1] == username and credentials[2] == password:
                    print("Login Successful\n")
                    role = credentials[3]

                    #The menu based on the role
                    #This is the admin menu
                    if role == 'admin':
                        while True:
                            print("\n \tWelcome to Admin Menu\n")
                            print("1.Add Groceries \n2.Display Groceries \n3.Search Groceries \n4.Modify "
                                  "Grocery Information \n5.Delete Groceries \n6.Stock Taking \n7.View Replenish List "
                                  "\n8.Exit")
                            choice = int(input("\nEnter Choice: "))
                            if choice == 1:
                                admin.admin_add()
                            elif choice == 2:
                                admin.display_groc()
                            elif choice == 3:
                                admin.search()
                            elif choice == 4:
                                admin.modify()
                            elif choice == 5:
                                groc_id = input("Please enter the ID of grocery you wish to delete: ")
                                admin.remove(groc_id)
                            elif choice == 6:
                                admin.stock_take()
                            elif choice == 7:
                                admin.view_replenish_list()
                            elif choice == 8:
                                break
                            else:
                                print("Invalid input. \n Please enter an option from 1-8: ")

                    #This is the Inventory Checker Menu 
                    elif role == 'inventory-checker':
                        while True:
                            print("\n \tWelcome to Inventory Checker Menu\n")
                            print("1.Stock Taking \n2.Search \n3.Exit")
                            choice = int(input("\nEnter Choice: "))
                            if choice == 1:
                                ic.stock_take()
                            elif choice == 2:
                                ic.search()
                            elif choice == 3:
                                break
                            else:
                                print("Invalid input. \n Please enter an option again: ")

                    #This is the Purchaser
                    elif role == 'purchaser':
                        while True:
                            print("\n\t Welcome to Purchaser Menu\n")
                            print("1. Stock Replenishment \n2. Exit")
                            choice = int(input("\nEnter your choice: "))
                            if choice == 1:
                                purchaser.stock_replenishment()
                            elif choice == 2:
                                break
                            else:
                                print("Invalid input. Please enter an option again: ")

                    break
            else:
                print("Incorrect username or password. Try again.")

    elif choice == 0:
        exit()

    else:
        print("Invalid input. Try again.")
