import filehandler as f

#Defining a function that adds groceries by getting the details from user and adds to a list called item.
#The function then calls the groc_writer from filehandler and appends to the text file
def admin_add():
    print("Enter the following details about the groceries: ")
    code = (input("Enter code: "))
    desc = input("Description: ")
    print("\n Please choose a category: \n\t1.Vegetable \n\t2.Fruit \n\t3.Snacks \n\t4.Dairy \n\t5.Meat")
    choice = int(input("Category: "))
    if choice == 1:
        category = 'Vegetable'
    elif choice == 2:
        category = 'Fruit'
    elif choice == 3:
        category = 'Snacks'
    elif choice == 4:
        category = 'Dairy'
    elif choice == 5:
        category = 'Meat'

    unit = input("Unit: ")
    price = (input("Price: "))
    quantity = (input("Quantity: "))
    minimum = (input("Min: "))

    item = [code, desc, category, unit, price, quantity, minimum]

    f.groc_writer(item)
    print("Grocery added successfully")

#Creating a function to display the groceries from the text file using the read_groceries function from filehandler
def display_groc():
    run = "Y"
    while run == "Y":
        f.read_groceries()
        run = input("\n\t Enter Y to display again, press any other key to exit: ")

#Function to remove the grocery from the text file
def remove(grocery_id):
    run = 'Y'
    while run == "Y":
        with open('groceries.txt', 'r') as f:
            lines = f.readlines()

        with open('groceries.txt', 'w') as f:
            for line in lines:
                if not line.startswith(str(grocery_id)):
                    f.write(line)
        print("Successfully Deleted")
        run = input("\n\t Enter Y to delete again, press any other key to exit: ")

#Function to modify the details of the grocery
def modify():
    with open("groceries.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            grocery = line.strip().split("\t")
            print("\n ",
                  f"ID: {grocery[0]}, Name: {grocery[1]}, Category: {grocery[2]}, Unit: {grocery[3]}, Price: {grocery[4]}, Quantity: {grocery[5]}, Minimum Quantity: {grocery[6]}")
            update_choice = input("Do you want to update this grocery (Y/N)? ")
            if update_choice.lower() == "y":
                print("1. Grocery ID")
                print("2. Name")
                print("3. Category")
                print("4. Unit")
                print("5. Price")
                print("6. Quantity")
                print("7. Minimum Quantity")

                field_choice = input("Which field do you want to update (1-7)? ")
                if field_choice == "1":
                    new_id = input("Enter the new grocery ID: ")
                    grocery[0] = new_id
                elif field_choice == "2":
                    new_name = input("Enter the new grocery name: ")
                    grocery[1] = new_name
                elif field_choice == "3":
                    new_category = input("Enter the new grocery category: ")
                    grocery[2] = new_category
                elif field_choice == "4":
                    new_unit = input("Enter the new grocery unit: ")
                    grocery[3] = new_unit
                elif field_choice == "5":
                    new_price = input("Enter the new grocery price: ")
                    grocery[4] = new_price
                elif field_choice == "6":
                    new_quantity = input("Enter the new grocery quantity: ")
                    grocery[5] = new_quantity
                elif field_choice == "7":
                    new_min_qty = input("Enter the new grocery minimum quantity: ")
                    grocery[6] = new_min_qty
                else:
                    print("Invalid choice. Try again.")
                    continue
            new_line = "\t".join(grocery) + "\n"
            f.write(new_line)
        f.truncate()

#Used to search the groceries.txt file based on user criteria.
#A Few options are: Item Description, Code Range, Category, Price Range
def search():
    run = "Y"
    while run == "Y":
        print("\nChoose what you would like to search by: \n \t1. Item Description \n\t 2. Code Range \n\t 3. Category "
              "\n\t 4. Price Range \n\t 0. Exit")
        choice = int(input("Choice: "))

        #Searching by Description
        if choice == 1:
            description = input("Enter the description you are looking for: ")
            exist = False
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if description.lower() in details[1].lower():
                        print(line)
                        exist = True
            if not exist:
                print("Sorry the item with that description does not exist")

        #Searching by Code Range
        elif choice == 2:
            exist = False
            up_range = int(input("\nEnter upper code range: "))
            low_range = int(input("Enter lower code range: "))
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if low_range <= int(details[0]) <= up_range:
                        print(line)
                        exist = True
            if not exist:
                print("Sorry, item code in that range does not exist")

        #Searching by Category
        elif choice == 3:
            exist = False
            print("\tVegetable \n\tFruit \n\tSnacks \n\tDairy \n\tMeat")
            categ = (input("Choose a Category: "))
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if details[2] == categ:
                        print(line)
                        exist = True
            if not exist:
                print("Sorry, item in that category does not exist")

        #Searching by Price Range
        elif choice == 4:
            exist = False
            price_low = float(input("\nEnter lower price range: "))
            price_up = float(input("Enter upper price range: "))
            with open("groceries.txt", "r") as file:
                for line in file:
                    details = line.split()
                    if price_low <= float(details[4]) <= price_up:
                        print(line)
                        exist = True
            if not exist:
                print("Sorry, item code in that range does not exist")

        elif choice == 5:
            break

        run = input("\n\t Enter Y to search again, press any other key to exit: ")

#Defining a function to modify the quantities of stock
def stock_take():
    run = "Y"
    while run == "Y":
        item_code = input("Enter item code: ")
        with open("groceries.txt", "r") as file:
            found = False
            for line in file:
                details = line.split()
                if item_code == details[0]:
                    found = True
                    print("Item:", details[1])
                    print("Available quantity:", details[5])
                    new_quantity = input("Enter new quantity: ")
                    details[5] = new_quantity
                    break
        if not found:
            print("Item does not exist.")
            return
        with open("groceries.txt", "r") as file:
            lines = file.readlines()
        with open("groceries.txt", "w") as file:
            for line in lines:
                if item_code == line.split()[0]:
                    file.write("\t".join(details) + "\n")
                else:
                    file.write(line)
        print("Quantity updated successfully.")

        run = input("\n\t Enter Y to modify again, press any other key to exit: ")

#Function to check which groceries needs to be refilled.
def view_replenish_list():
    run = "Y"
    while run == "Y":
        enough = True

        with open("groceries.txt", "r") as file:
            for line in file:
                details = line.split()
                if (details[6]) >  (details[5]):
                    print(line)
                    enough = False
        if enough:
            print("Quantities are fine")

        run = input("\n\t Enter Y to search again, press any other key to exit: ")
